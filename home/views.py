from django.shortcuts import render, redirect
# Create your views here.

def home_page(request):
    context = {}
    return render(request, 'home/home.html', context)