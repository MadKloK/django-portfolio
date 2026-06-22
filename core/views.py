from django.shortcuts import render
from .data import data

# Create your views here.

def index_view(request):
    context = data
    return render(request, "index.html", context=context)