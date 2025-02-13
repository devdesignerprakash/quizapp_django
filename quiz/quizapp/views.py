from django.shortcuts import render,get_object_or_404
from .models import*

def home_view(request):
    return render(request,'app/home.html')

# Create your views here.

def category_view(request):
    categories = Category.objects.all() 
  
    context = {
       "categories": categories
    }
    return render(request, 'app/categories.html', context)
def questions_view(request,category_id):
    category = get_object_or_404(Category, id=uuid.UUID(str(category_id))) 
    questions = Question.objects.filter(category=category).prefetch_related('choices')
    print(questions)
    total_time = sum(question.time_limit for question in questions)
    context={
        "questions":questions,
        "category":category,
        "total_time":total_time
    }
    return render(request, 'app/questions.html',context)
def answer_check_view(request):
    print("answer check *********************")
    if request.method=="POST":
       user_answers= request.POST
       