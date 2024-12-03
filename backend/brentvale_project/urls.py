"""
URL configuration for brentvale_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core_views  # Import views from core
from tasks import views as tasks_views  # Import views from tasks
from core import views as core_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     # Document-related URLs handled by core app
#     path('documents/', core_views.document_list, name='document_list'),
#     path('upload/', core_views.document_upload, name='document_upload'),
    
#     # Task-related URLs handled by tasks app
#     path('task/create/', tasks_views.task_create, name='create_task'),
#     path('tasks/', include('tasks.urls')),  # Task-related URLs handled by tasks app
    
#     # Root URL points to task list view from tasks app
#     path('', tasks_views.task_list, name='home'),  # Default route points to task list view

    

# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/documents/', include('documents.urls')),  # Preferred (Separate app for documents)
    path('api/shipments/', include('shipments.urls')),  # Preferred (Separate app for shipments)
    path('api/dashboard/', include('dashboard.urls')),  # Dashboard functionality
    path('tasks/', include('tasks.urls')),  # Task-related functionality
]