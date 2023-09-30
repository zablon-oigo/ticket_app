from django.urls import path
from .views import *

urlpatterns=[
    path('register-customer/',register_customer, name='register-customer'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]