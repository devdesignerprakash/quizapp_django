from django.urls import path,include
from .import views

urlpatterns = [
    path('dashboard/',views.admin_dashboard_view, name='admin_dashboard')
]
