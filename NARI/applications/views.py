from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 'Feature 1'
    feature1.name = 'EXPLORE YOURSELF'
    feature1.details = 'Only 5 minutes! Answer some questions and discover more about you.'

    feature2 = Feature()
    feature2.id = 'Feature 2'
    feature2.name = 'NARI'
    feature2.details = 'Struggling with tons of problems and don\'t know who to talk to? Sort through them with NARI.'

    feature3 = Feature()
    feature3.id = 'Feature 3'
    feature3.name = 'LABORATORY'
    feature3.details = 'Pick a course and learn more about our metal health.'

    feature4 = Feature()
    feature4.id = 'Feature 4'
    feature4.name = 'SAFE ENVIRONMENT'
    feature4.details = 'Be sure to keep the environment friendly. Treat others with kindness and respect.'

    return render(request, 'index.html', {'feature1': feature1, 'feature2': feature2, 'feature3': feature3, 'feature4': feature4})

def counter(request):
    return render(request, 'counter.html')