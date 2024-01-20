from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import *
from .analize import * 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required,user_passes_test

 
def login_page(requests):
    if requests.method == "POST":
        data= requests.POST            
        user_name= data['uname']
        password= data['psw']
        
        if not User.objects.filter(username= user_name).exists():
            messages.add_message(requests, messages.INFO, "Invalid User name")
            return redirect('home_page')
        user= authenticate(username= user_name, password= password)
        if user is None:
            messages.add_message(requests, messages.INFO, "Invalid Password")
            return redirect('home_page')            
        else:
            messages.add_message(requests, messages.INFO, "Success")
            login(requests,user) #session send
            return redirect('analize')

    return render(requests, "html_page/analize.html")

def logout_page(requests):
    logout(requests)  

    return redirect('home_page')
 
def register(requests):
    if requests.method=="POST":
        print("went in")
        data = requests.POST
        user_name= data['urname']
        email=data['uremail']
        password= data['urpass']


        if User.objects.filter(username= user_name).exists():
            messages.add_message(requests, messages.INFO, "User already Exits plz try again.")
            print("User already Exits plz try again.")
            redirect_url = reverse('home_page') + '?show_login_popup=true'
            return  HttpResponseRedirect(redirect_url) #redirect('home_page')
        else:
            messages.add_message(requests, messages.INFO, "Account Created Sucessfully")
            print("Account Created Sucessfully")
            user = User.objects.create(username=user_name, email =email, password= password)
            user.set_password(password)
            user.save()
            login(requests,user)
            return redirect('analize')
 
    return render(requests,"html_page/analize.html")

def list_soil(request):
    if request.method== "POST":
        data= request.POST
    return render(request, "html_page/list_soil.html")

def store_data(request):
    if request.method== "POST":
        data= request.POST

        All_soil.objects.create(soil_image= request.FILES.get('image'), soil_name=data.get('imageName'), soil_discription=data.get('soilDescription'))
    return render(request,"html_page/another.html")

def home_page(request):
    return render(request,"html_page/index.html")

@login_required(login_url="home_page")
def test_report(request):
    if request.method== "POST":
        data= request.POST
        soil_location= data['city']
        soil_name=data['soilName']
        soil_discription=data['soil_discp']
        soil_image= request.FILES.get('image')
        user = get_object_or_404(User, username=request.user.username)
        Test_soil.objects.create(usersd=user,soil_image=soil_image,soil_discription=soil_discription, soil_location=soil_location,soil_name_col=soil_name)

        return redirect('analize')

    return render(request, "html_page/test_soil.html")

def case_report(request):
    user = get_object_or_404(User, username=request.user.username)
    test_soil_list= Test_soil.objects.filter(usersd=user)
    
    return render(request,"html_page/case.html", {"all_data": test_soil_list})

def profile_report(requests):
    if requests.method == "POST":
        data= requests.POST             
        user_name= data['uname']
        email=data['uremail']
        password= data['psw']
        
        user= authenticate(username= user_name, password= password)
        if user is None:
            print('passss')
            messages.add_message(requests, messages.INFO, "Invalid Password")
            return redirect('profile')            
        else:
            user = User.objects.get(username= user_name)
            user.email=email
            user.save()
            return redirect('home_page')

    return render(requests,"html_page/profile.html")

def analize(request):
    test_soil_obj= Test_soil.objects.all()
    user_has=False
    for all_test in test_soil_obj:
        print(str(request.user.username) == str(all_test.usersd),(),(all_test.usersd))
        if str(request.user.username) == str(all_test.usersd):
            soil_name_col= all_test.soil_name_col
            discription= soil_infO(soil_name_col)
            crops= list(recommend_crops(soil_name_col))
            to_Do_not_do = soil_safety_guidelines(soil_name_col)
            all_med={}
            all_tool={}
            for each_crop in crops:
                tools= recomend_tools(each_crop)
                medicine= recomend_medicine(each_crop)
                all_tool.update({each_crop:tools})
                all_med.update({each_crop:medicine})
            percentage= productive_quality(soil_name_col)
            context= {'discription':discription,'crops':crops,'percentage':percentage, 'medi':all_med, "tools":all_tool, "to_Do_not_do":to_Do_not_do }
            user_has=True
    if not user_has:
        return redirect('test')    
    return render(request,"html_page/analize.html",context=context)