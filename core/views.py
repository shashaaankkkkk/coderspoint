from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def hello(request):
    return JsonResponse({"message":"hello"},safe=False)
def index(request):
    return render(request,"index.html")