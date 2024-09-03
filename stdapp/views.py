from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    all_std =std.objects.all()
    context = {
        'all_std':all_std
    }
    return render(request,'index.html',context)