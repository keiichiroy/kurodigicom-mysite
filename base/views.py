from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def top(request):
  return HttpResponse('Hello world!')
