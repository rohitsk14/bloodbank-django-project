from django.shortcuts import render,redirect
from users.models import profile
from .forms import requestform,messageform
from django.contrib import messages

def search(request):
    return render(request,'home.html')


def find(request):
    p=profile.objects.all()
    city = request.POST["city"]
    blood_group = request.POST["blood_group"]
    for d in p:
        if d.blood_group == blood_group and d.city == city:
            return render(request, 'searched.html', {'name': d.name, 'mob': d.mob_no})
    else:
        return render(request, 'searched.html')

def request(request):
    if request.method == 'POST':
        form = requestform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Request has been accepted.')
            return redirect('request')
    else:
        form = requestform()
    return render(request,'request.html',{'form':form})


def contact(request):
    if request.method == 'POST':
        form = messageform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Message sent')
            return redirect('contact')
    else:
        form = messageform()
    return render(request,'contact.html',{'form':form})



