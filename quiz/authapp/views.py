from django.shortcuts import render

def admin_dashboard_view(request):
    return render(request,'app/dashboard_view.html')

# Create your views here.
