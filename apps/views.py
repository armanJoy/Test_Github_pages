from django.shortcuts import render
from django.http import  HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

def apps(request):
    return render(request, 'apps_index.html', context=None )