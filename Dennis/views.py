from django.shortcuts import render
from Dennis.form import EmpForm


def Home(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'aboutus.html')


def Contact(request):
    return render(request, 'contactus.html')


def myform(request):
    stu = EmpForm()
    return render(request, 'forms.html', {'form': stu})
