from django.urls import path
from .views import *

urlpatterns=[
    path('',home_page, name="home_page"),
    path('login/', login_page, name= "login"),
    path('logout/', logout_page, name= 'logout'), 
    path('register/', register, name= 'register'),
    path('analize/', analize, name= 'analize'),
    path('test/', test_report, name= 'test'), 
    path('case/', case_report, name= 'case'),
    path('profile/', profile_report, name= 'profile'),
    
    # path('store_data',store_data, name="store_data")
]