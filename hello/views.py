from django.shortcuts import render

# Create your views here.

def template(request):
    return render(request, 'hello/template.html')

def form(request):
    return render(request, 'hello/form.html')