from dis import dis
from typing import Counter
from django import http
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from django.http import request
from django.shortcuts import redirect, render
from .models import menu_card
from django.http import HttpResponse
from cos.models import Order
from datetime import date,datetime
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.urls import reverse
from django.views.decorators.cache import never_cache
import pywhatkit
# Create your views here.
def frontpage(request):
    if request.user.is_authenticated:
        return redirect('adminportal')
    return render(request, 'cos/frontpage.html')

def shedule(request):
    return render(request,'cos/shedule.html')
def shedulemeal(request):
    print(request)
    return render(request,'cos/shedule.html')
def home(request):
    if request.user.is_authenticated:
        return render(request,'cos/frontpage.html')
    return redirect('frontpage')
def menucard(request):
    menu=menu_card.objects.all()
    menucard={"menu":menu}
    return render(request,'cos/menucard.html',menucard)
def info(request):
    return render(request,'cos/info.html')
def info1(request):
    if(request.method=="POST"):
        # today_order=Order.objects.filter(orderdate=date.today())
        first_name= request.POST.get('First_Name')
        last_name=request.POST.get("Last_Name")
        num=request.POST.get('phoneno')
        if len(num)!=10:
            messages.error(request,"Phone Number should be exctly 10 numbers!")
            return redirect('frontpage')
        try:
            obj=Order.objects.get(first_name=first_name,last_name=last_name,phoneno=num)
            messages.error(request,'Your todays dinner is already scheduled!')
            return redirect('frontpage')
        except :
            dic={}
            dic['first_name']=first_name
            dic['last_name']=last_name
            dic['phoneno']=num
            return render(request,'cos/shedule.html',dic)
    else:
        return HttpResponse("Error check your conections!")
def shedule1(request):
    if(request.method=='POST'):
        dic={}
        dic['timeslot']=request.POST.get('t')
        dic['mem']=request.POST.get('sel')
        dic['first_name']=request.POST.get('first_name')
        dic['last_name']=request.POST.get('last_name')
        dic['phoneno']=request.POST.get('phoneno')
        menu=menu_card.objects.all()
        dic['menu']=menu
        return render(request,'cos/menucard.html',dic)
    else:
        return HttpResponse("Khatam!")
def order(request):
    dic={}
    dish_l=[]
    dish_q=[]
    dish_p=[]
    if request.method=="POST":
        dic['timeslot']=request.POST.get('t')
        dic['mem']=request.POST.get('sel')
        dic['first_name']=request.POST.get('first_name')
        dic['last_name']=request.POST.get('last_name')
        dic['phoneno']=request.POST.get('phoneno')
        menu=menu_card.objects.all()
        for i in menu:
            dic1={}
            menu=menu_card.objects.all()
            dic['menu']=menu
            dish=request.POST.get(i.dish_name)
            l=len(request.POST.get(i.image))
            q=request.POST.get(i.image)
            # try:
            #     c=len(dish)
            # except: 
            #     messages.error(request,"None of the items has selected!")
            
            if(dish!=None and l==0):
                messages.error(request,'Items as well as the quantity should also be selected')
                return render(request,'cos/menucard.html',dic)
            elif(dish!=None):
                dish_l.append(dish)
                dish_q.append(q)
                dish_p.append(i.dish_price)
        sum=0
        for i in range(len(dish_q)):
            sum+=int(dish_q[i])*int(dish_p[i])
        
        # wattsapp messaging
        # max_len=0
        # for i in dish_l:
        #     if len(i)>max_len:
        #         max_len=len(i)
        # st='Dish'+"            "+"Quantity"+"    "+"Price\n"
        # for i in range(len(dish_l)):
        #     st+=str(dish_l[i])+"     "+str(dish_q[i])+"   "+str(dish_p[i])+"\n"
        # st+="Total="+str(sum)
        # p_string="+91"+str(dic['phoneno'])
        # l=str(datetime.now().time()).split(":")
        # pywhatkit.sendwhatmsg(p_string,st,int(l[0]),int(l[1])+1)
        # -------------------------------------------
        dish_l=','.join(dish_l)
        dish_q=','.join(dish_q)
        dish_p=','.join(dish_p)
        order1=Order(first_name=dic['first_name'],last_name=dic['last_name'],phoneno=dic['phoneno'],orderdate=date.today(),sheduletime=dic['timeslot'],dish_list=dish_l,quantity_list=dish_q,price_list=dish_p,members=dic['mem'],total=sum)
        order1.save()
        messages.success(request,"Your Dinner has been scheduled!")
        return redirect("home")
    else:
        return HttpResponse("NOT GET")
def just(request):
    orders=Order.objects.all()
    dic={'orders':orders}
    for i in orders:
        i.dish_list=i.dish_list.split(',')
    return render(request,'cos/info.html',dic)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminlogin(request):
    if request.method=="POST":
        usernmae=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=usernmae, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('adminportal')
        else:
            return HttpResponse('<h1>Invalid Credentials. Please Try Again.</h1>')
    
    return HttpResponse("adminportal")
def adminportal(request):
    if request.user.is_authenticated:
        order=Order.objects.filter(orderdate=date.today())
        dic={"order":order}
        for i  in order:
            i.dish_list=i.dish_list.split(',')
            i.quantity_list=i.quantity_list.split(',')
            i.price_list=i.price_list.split(',')
        return render(request,'cos/adminportal.html',dic)
    return redirect('frontpage')
def menucard1(request):
    dic={}
    menu=menu_card.objects.all()
    dic['menu']=menu
    return render(request,'cos/menucard.html',dic)
def adminlogout(request):
    logout(request)
    return redirect('frontpage')
def gotoadd(request):
    if request.user.is_authenticated:
        return render(request,"cos/add.html")
    return HttpResponse("NOT A Super User")
@csrf_exempt
def add(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            dishname=request.POST.get("dishname")
            dishprice=request.POST.get("dishprice")
            dishimage=request.FILES["dishimage"]
            menu=menu_card.objects.filter(dish_name=dishname)
            list_dish=list(menu_card.objects.all().values('dish_name'))
            just_list=[i[j] for i in list_dish for j in i]
            for i in range(len(just_list)):
                just_list[i]=just_list[i].lower()
                just_list[i]="".join(just_list[i].split())
            ref=dishname
            ref=ref.lower()
            ref="".join(ref.split())
            print(dishname)
            print(ref)
            print(just_list)
            if ref not in just_list:
                newitem=menu_card(dish_name=dishname,dish_price=dishprice,image=dishimage,dish_type="Fast Food")
                newitem.save()
                messages.success(request,"The dish has been add to the menucard!")
                return render(request,"cos/add.html")
            messages.error(request,"Dish is Alreadey in menucard! So it can not be added again!")
            return render(request,"cos/add.html")
        return render(request,"cos/add.html")
    return HttpResponse("not admin")
def gotodelete(request):
    if request.user.is_authenticated:
        menus=menu_card.objects.all()
        dic={}
        dic["menus"]=menus
        return render(request,"cos/delete.html",dic)
    return HttpResponse("Not admin")
def deteteitem(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            dishname=request.GET.get("dishname")
            item=menu_card.objects.filter(dish_name=dishname)
            # item.delete()
            print(item)
            messages.success(request,"Items has been deleted from menucard!")
            return redirect("gotodelete")
        return HttpResponse("not a get method")
    return HttpResponse('Not admin')