from django.shortcuts import render
from .models import*

def home_view(request):
    return render(request,'app/home.html')

# Create your views here.

def category_view(request):
    categories = Category.objects.all()  
    print(categories)
    context = {
       "categories": categories
    }
    return render(request, 'app/categories.html', context)