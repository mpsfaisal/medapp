from django.urls import path
from .views import Patient_history 
from .views import AuthorUpdate
from . import views
import os
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import UpdateView



app_name='medapp'

urlpatterns = [ 
	path('',views.index, name='index'),
	path('AuthorUpdate/<int:pk>/',AuthorUpdate.as_view(),name='Patient_history'),
	path('Patient_history/',login_required(Patient_history.as_view()),name='Patient_history'),
	path('new_patient_registor/',views.new_patient_registor, name='new_registor'),
	#path('Patient_history/',views.Patient_history, name='Patient_history'),
	path('registor/',views.registor, name='registor'),
	path('update/<int:id>/',views.update, name='update'),
	path('patient_update/<int:id>/',views.patient_update, name='patient_update')

]

