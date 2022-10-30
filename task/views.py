from django.shortcuts import render
from django.http import JsonResponse

def home_view(request):
  post = {
    "slackUsername": "bemjoe",
    "backend": True,
    "age": 22,
    "bio": "Trying to get good at backend development"
  }
  
  
  return JsonResponse(post)
