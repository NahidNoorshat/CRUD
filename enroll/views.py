from django.shortcuts import render, HttpResponseRedirect
from .forms import studentRegestration
from .models import user

# Create your views here.

def addhere(request):
    if request.method == 'POST':
        fm = studentRegestration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = studentRegestration()
    else:
        fm = studentRegestration()
    stud = user.objects.all()

    return render(request, 'enroll/add.html', {'form':fm, 'stu': stud})

def update(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = studentRegestration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = studentRegestration(instance=pi)
    return render(request, 'enroll/update.html', {'form': fm})

def delet_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
