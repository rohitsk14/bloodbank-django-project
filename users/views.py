from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import userregisterform,userupdateform
from django.contrib.auth.decorators import login_required
from users import mail
from .models import otp
import random
import hashlib


def register(request):
    if request.method == 'POST':
        form=userregisterform(request.POST)
        if form.is_valid():
            x = otp()
            username = form.cleaned_data.get('username')
            x.username = username
            email = form.cleaned_data.get('email')
            x.email = email
            x.password = form.cleaned_data.get('password1')
            ot = random.randint(99999, 999999)
            x.otp = ot
            x.save()

            subject = "OTP-This is an system generated e-mail.Do not reply to this e-mail."
            body = f"Otp for registration is {ot}."
            msg = f"Subject:{subject}\n\n{body}"
            mail.sendmail(email, msg)
            return render(request,'varify.html',{'username':username})
    else:
        form=userregisterform()
    return render(request,'users/register.html',{'form':form})


def varify(request):
    if request.method=='POST':
        ot = request.POST["otps"]
        username = request.POST["username"]
        u=User()
        x = otp.objects.all()
        for i in x:
            if i.username == username or i.otp == ot:
                u.username = i.username
                # s=i.password
                # hs = hashlib.sha256(s.encode('utf-8')).hexdigest()
                u.set_password(i.password)
                u.email = i.email
                u.save()
                messages.success(request,f'account created for {username}')
                return redirect('login')
        else:
            messages.success(request, 'Enter valid OTP')
        return render(request, 'varify.html',{'username':username})

# def register(request):
#     if request.method == 'POST':
#         form=userregisterform(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get( 'username')
#             messages.success(request,f'account created for {username}')
#             form.save()
#             return redirect('login')
#
#     else:
#         form=userregisterform()
#     return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form = userupdateform(request.POST,instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,'Profile updated Successfully')
            redirect('profile')
    else:
        u_form = userupdateform(instance=request.user.profile)
    return render(request,'users/profile.html',{'form':u_form})

