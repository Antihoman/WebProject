from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def mainPage(request):
    context = {'questions': models.QUESTION}
    return render(request, 'mainPage.html', context)

def answerPage(request, question_id):
    context = {'question': models.QUESTION[question_id]}
    return render(request, ('answerPage.html'), context)