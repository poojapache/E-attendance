from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout

def index(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request, 'home/index.html', {})
