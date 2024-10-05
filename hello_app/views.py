from django.http import HttpResponse
import html

def hello(request, name):
    return HttpResponse(f"Hello, {name}")

def hello2(request):
    name = request.GET['name']
    return HttpResponse(f"Hello, {name}")

def calc(request, a, b):
    return HttpResponse("A*B=" + str(a*b))