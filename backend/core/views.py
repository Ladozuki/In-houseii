# views.py
from django.shortcuts import render
from core.models import Task, Document, Shipment, User
from django.db.models import Q
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from brentvale_project.serializers import DocumentSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models

# views.py (Stakeholder Access Control)
from django.contrib.auth.decorators import permission_required


def document_list(request):

    search_query = request.GET.get('search', '')
    document_type = request.GET.get('document_type', '')
    status = request.GET.get('status', '')
    created_at = request.GET.get('created_at', '')

    documents = Document.objects.all()

    if search_query:
        documents = documents.filter(shipment_id__icontains=search_query)

    if document_type:
        documents = documents.filter(document_type=document_type)

    if status:
        documents = documents.filter(status=status)

    if created_at:
        documents = documents.filter(created_at__date=created_at)

    return render(request, 'document_list.html', {'documents': documents})

def view_document(request, document_id):
    try:
        document = Document.objects.get(id = document_id)
    except Document.DoesNotExist:
        raise Http404("Document not found")
    
    return render(request, 'document_detail.html', {'document': document})

@api_view(['GET'])
def dashboard_data(request):
    data = {
        "total_documents": Document.objects.count(),
        "documents_by_status": Document.objects.values('status').annotate(count=models.Count('status')),
        "shipments_by_status": Shipment.objects.values('customs_status').annotate(count=models.Count('customs_status')),
    }


@api_view(['POST'])
def document_upload(request):
    if request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        shipment_id = request.data.get('shipment_id')
        assigned_to = request.data.get('assigned_to')
        task_description = request.data.get('task_description')

        shipment = Shipment.objects.get(id=shipment_id)
        assigned_user = User.objects.get(id=assigned_to)

        task = Task.objects.create(
            shipment=shipment,
            assigned_to=assigned_user,
            task_description=task_description
        )
        return JsonResponse({"task_id": task.id}, status=201)



