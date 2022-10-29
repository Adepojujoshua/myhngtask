from django.shortcuts import render

def home_view(request):
  post = {
    "slack_username": "bemjoe",
    "backend": "true",
    "age": 22,
    "bio": "Trying to get good at backend development"
  }
  
  context = {
    "post": post,
  }
  
  return render(request, 'task/index.html', context)
