from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout


def registor_users(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #login the user
            login(request,user)
            return redirect('medapp:index')
    else:
        form=UserCreationForm()

    return render(request,'registor_users.html',{'form':form})

def users_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('medapp:index')
    else:

        form=AuthenticationForm()

    return render(request,'login.html',{'form':form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('medapp:index')
    else:
        return redirect('medapp:index')

def base(request):
    return render(request,'base.html')