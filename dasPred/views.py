from django.shortcuts import render

# Create your views here.

def teststress(request):
    return render(request, 'teststress.html')