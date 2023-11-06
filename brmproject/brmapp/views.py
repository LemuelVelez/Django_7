from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloView(request):
    return render(request,"viewbook.html")