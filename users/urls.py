from django.urls import path
from . import views
import os

app_name='users'

urlpatterns = [ 
	path('registor_users/',views.registor_users, name='registor_users'),
	path('users_login/',views.users_login, name='users_login'),
	path('user_logout/',views.user_logout, name='user_logout'),
	path('base/',views.base, name='base'),	

]
