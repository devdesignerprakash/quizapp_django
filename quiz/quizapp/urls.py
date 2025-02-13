
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('category/',views.category_view, name="category"),
    path("questions/<uuid:category_id>/", views.questions_view, name="questions_page"),
    
]