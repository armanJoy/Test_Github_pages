from django.shortcuts import render
from django.http import  HttpResponse

from .models import Match_Regi

from django.views import generic

from django_ajax.decorators import ajax
# Create your views here.

def cricket(request):
    return HttpResponse("Its Cricket Page.")
#
# def score(request):
#     return HttpResponse("Its Live Score Page.")

@ajax
def abc(request):
    c = 2 + 3
    return c

def base(request):
    return render(request, 'base.html', context=None)

def sample(request):
    return render(request, 'sample.html', context=None)



class MatchRegistrationView(generic.ListView):

    model = Match_Regi
