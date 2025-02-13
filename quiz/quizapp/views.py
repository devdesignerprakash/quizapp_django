from django.shortcuts import render,get_object_or_404
from .models import*
import uuid

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

def result_check_view(request):
    if request.method == "POST":
        user_answers = request.POST
        correct_count = 0
        total_questions = 0
        results = []
        for key, value in user_answers.items():
            key_parts = key.split("_")
            if len(key_parts) > 1:
                try:
                    question_id = uuid.UUID(key_parts[1])  # Convert to UUID
                except ValueError:
                    print(f"Invalid UUID format for question_id: {key_parts[1]}")
                    continue  

                selected_choice_id = value
                question = get_object_or_404(Question, id=question_id)
                selected_choice = get_object_or_404(Choice, id=selected_choice_id)
                correct_answer = get_object_or_404(Answer, question=question)

                is_correct = selected_choice == correct_answer.choice
                if is_correct:
                    correct_count += 1
                
                total_questions += 1 
                print("total questions",total_questions)

                results.append({
                    "question": question,
                    "selected_answer": selected_choice,
                    "correct_answer": correct_answer.choice,
                    "is_correct": is_correct
                })
        score_percentage = (correct_count * 10) if total_questions else 0
        
        context = {
            "results": results,
            "score": score_percentage,
            "total_questions_attempt":total_questions
        }
        return render(request, 'app/result.html', context)
    return render(request, 'app/result.html')
