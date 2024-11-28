from django.db import models
from django.contrib.auth.models import User  # Assuming default Django User model

# Document Model
class Document(models.Model):
    DOCUMENT_TYPES = [
        ('customs', 'Customs Document'),
        ('internal', 'Internal Document'),
        ('shipment', 'Shipment Document'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=255)
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPES)
    upload = models.FileField(upload_to='documents/')
    metadata = models.JSONField(blank=True, null=True)  # To store dynamic attributes like tags, approval history, etc.
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_document_type_display()}) - {self.status}"
    
    def rollback_to_version(self, version_number):
        version = self.versions.filter(version_number=version_number).first()
        if version:
            self.upload = version.file
            self.save()
        return version
    
# Document Version Model for Version Control
class DocumentVersion(models.Model):
    document = models.ForeignKey(Document, related_name='versions', on_delete=models.CASCADE)
    version_number = models.IntegerField()
    file = models.FileField(upload_to='document_versions/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Version {self.version_number} of {self.document.title}"

# Shipment Model
class Shipment(models.Model):
    CUSTOMS_STATUSES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('cleared', 'Cleared'),
        ('delayed', 'Delayed'),
    ]

    shipment_id = models.CharField(max_length=50, unique=True)
    client_name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    customs_status = models.CharField(max_length=50, choices=CUSTOMS_STATUSES, default='not_started')
    associated_documents = models.ManyToManyField(Document, blank=True, related_name='shipments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shipment {self.shipment_id} - {self.customs_status}"

# Additional Features for Search and Advanced Functionality
class MetadataSearch(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE, related_name="metadata_search")
    search_keywords = models.TextField()  # Can store extracted keywords for enhanced searching
