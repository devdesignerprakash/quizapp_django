from django.db import models
import uuid

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    category_image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    category = models.ForeignKey(Category, related_name='questions',null=True, blank=True, on_delete=models.CASCADE)
    time_limit= models.IntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.OneToOneField(Question, related_name='answer', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Answer to {self.question.text}: {self.choice.text}"

# Create your models here.


# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
# from .models import Question, Choice, Answer

# def answer_check_view(request):
#     if request.method == "POST":
#         print("Answer check *********************")

#         user_answers = request.POST  # Dictionary of submitted answers
#         correct_count = 0  # Track correct answers
#         total_questions = 0
#         results = []  # Store results per question

#         for key, value in user_answers.items():
#             if key.startswith("question_"):  # Ensure processing only question-related data
#                 question_id = key.split("_")[1]  # Extract question ID
#                 selected_choice_id = value  # User's selected choice
                
#                 question = get_object_or_404(Question, id=question_id)
#                 selected_choice = get_object_or_404(Choice, id=selected_choice_id)
#                 correct_answer = get_object_or_404(Answer, question=question)

#                 is_correct = selected_choice == correct_answer.correct_choice  # Compare user choice with stored answer

#                 if is_correct:
#                     correct_count += 1
                
#                 total_questions += 1
                
#                 # Store result for response
#                 results.append({
#                     "question": question.text,
#                     "selected_answer": selected_choice.text,
#                     "correct_answer": correct_answer.correct_choice.text,
#                     "is_correct": is_correct
#                 })

#         # Calculate percentage
#         score_percentage = (correct_count / total_questions) * 100 if total_questions else 0

#         # Return JSON response with results
#         return JsonResponse({
#             "score": correct_count,
#             "total": total_questions,
#             "percentage": score_percentage,
#             "results": results
#         })

#     return JsonResponse({"error": "Invalid request"}, status=400)
