from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    all_std =std.objects.all()
    context = {
        'all_std':all_std
    }
    return render(request,'index.html',context)


def student_detail(request,Roll_No):
    single_student = std.objects.get(Roll_No = Roll_No)
    context ={
        'student':single_student
    }
    return render(request,'std_detail.html',context)