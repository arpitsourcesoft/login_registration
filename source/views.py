from django.http import HttpResponse
from django.shortcuts import render
from .models import User



# Create your views here.
def list(request):
    user_data = User.objects.all()
    return render(request, 'index.html', {'objects':user_data})

def details(request):
    val = User.objects.all()
    return render(request, 'index.html', {'object': val})


