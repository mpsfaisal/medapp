from django.shortcuts import render,redirect
from django.views.generic import ListView

from django.views.generic.edit import UpdateView
from .models import patient_details

from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse,request
from django.shortcuts import render,get_object_or_404
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.db import models
from .models import patient_details
from datetime import datetime
from .forms import Reg_patient

#@login_required(login_url='users:users_login')
#@method_decorator(login_required,name='Patient_history')
class Patient_history(ListView):
    model=patient_details
    #<app>/<model>_<view_type>.html
    template_name='Patient_history.html'
    context_object_name='myresult'
    paginate_by= 5

    
@login_required(login_url='users:users_login')
def index(request):
    if request.method == 'POST':
        form=Reg_patient(request.POST)
        if form.is_valid():
            form.save()
            #redirect('medapp:Patient_history')
            return render(request,'echo.html',{'res':form.fields.get('name')})
    else:
        form=Reg_patient()
    return render(request,'index.html',{'form':form})

@login_required(login_url='users:users_login')
def new_patient_registor(request):
    return render(request,'new_patient_registor.html')

"""@login_required(login_url='users:users_login')
def Patient_history(request):
    
    myresult=patient_details.objects.all()
    return render(request,'Patient_history.html',{'myresult':myresult})
"""
def patient_update(request,id):
    myresult=get_object_or_404(patient_details,pk=id)
    #myresult=patient_details2.objects.filter(id=id)
    return render(request,'patient_update.html',{'myresult' :myresult})


def registor(request):
    """name=request.POST["name"]
    phone=request.POST["phone"]
    Address=request.POST["address"]
    gender=request.POST["gender"]
    cd=request.POST["consulting_date"]
    history=request.POST["history"]
    observations=request.POST["observations"]
    remedy=request.POST["remedy"]
    nc=request.POST["next_consultation"]
    entry_by=request.POST["entry_by"]

    res_obj=patient_details(name=name,phone=phone,address=Address,gender=gender,consulting_date=cd,history=history,observations=observations,remedy=remedy,next_consultation=nc,entry_by=entry_by)
    """
    if request.method=='POST':

        res_obj=patient_details(request.POST)
        res_obj.save()
    return render(request,'echo.html',{'res':res_obj})


def update(request,id):
    name=request.POST["name"]
    phone=request.POST["phone"]
    Address=request.POST["Address"]
    gender=request.POST["gender"]
    cd=request.POST["consulting_date"]
    history=request.POST["history"]
    observations=request.POST["observations"]
    remedy=request.POST["remedy"]
    nc=request.POST["next_consultation"]
    entry_by=request.POST["entry_by"]

    res_obj=patient_details.objects.get(pk=id)
    res_obj.name=name
    res_obj.phone=phone
    res_obj.address=Address
    res_obj.gender=gender
    res_obj.consulting_date=cd
    res_obj.history=history
    res_obj.observations=observations
    res_obj.remedy=remedy
    res_obj.next_consultation=nc
    res_obj.entry_by=entry_by

    res_obj.save()
    return render(request,'echo.html',{'res':res_obj})

class AuthorUpdate(UpdateView):
    
    model = patient_details
    fields=['name','phone','gender','address','consulting_date','history','observations','remedy','next_consultation','entry_by']
    template_name_suffix = '_update_form'
    template_name='patient_details_update_form.html'
    

