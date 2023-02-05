from datetime import date
from django.conf import settings
from django.contrib import messages
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import Part_2, Part_3,Part_4
from elib.models import Book
from calendar import datetime
from django.views.decorators.csrf import csrf_exempt

import os


def AdmnUser(request):
    if request.user.is_authenticated:
        AppliedBooks = Part_3.objects.all()
        n=len(AppliedBooks)
        params = {'Book':AppliedBooks,'range':range(1,n)}
        return render(request, 'admn/AdmnUser.html',params)
    return redirect('frontpage')

def Records(request):
    if request.user.is_authenticated:
        record = Part_4.objects.all()
        n=len(record)
        params = {'Book':record,'range':range(1,n)}
        return render(request, 'admn/Records.html',params)
    return redirect('frontpage')


def Sanction(request,slug):
    if request.user.is_authenticated:
        l1= Part_3.objects.get(Book_id=int(slug))
        l2= Part_4(Book_id=l1.Book_id,Book_Name=l1.Book_Name,author=l1.author,applicantname=l1.applicantname,sactime=datetime.datetime.now().strftime("%c"))
        l2.save()
        l1.delete()
        messages.success(request,'Book Sanctioned Successfully')
        return redirect('AdmnUser') 
    return redirect('frontpage')

def Reject(request,slug):
    if request.user.is_authenticated:
        l1= Part_3.objects.get(Book_id=int(slug))
        l2= Part_2(Book_id=l1.Book_id,Book_Name=l1.Book_Name,author=l1.author)
        l2.save()
        l1.delete()
        messages.success(request,'Book Rejected Successfully')
        return redirect('AdmnUser')   
    return redirect('frontpage')

def Return(request,slug):
    if request.user.is_authenticated:
        l1= Part_4.objects.get(Book_id=int(slug),rettime='--')
        l2= Part_2(Book_id=l1.Book_id,Book_Name=l1.Book_Name,author=l1.author)
        l2.save()
        l1.rettime = datetime.datetime.now().strftime("%c")
        l1.save()
        messages.success(request,'Book Returned Successfully')
        return redirect('Records') 
    return redirect('frontpage')

def AdmnBooks(request):
    if request.user.is_authenticated:
        Books = Book.objects.all()
        n=len(Books)
        params = {'Book':Books,'range':range(1,n)}
        return render(request, 'admn/AdmnBooks.html',params)
    return redirect('frontpage')

def delete(request,slug):
    if request.user.is_authenticated:
        l1=Book.objects.get(Book_id=int(slug))
        l1.delete()
        l2=Part_2.objects.get(Book_id=int(slug))
        l2.delete()
        messages.success(request,'Book Deleted Successfully')
        return redirect('AdmnBooks')
    return redirect('frontpage')

def AddBook(request):
    if request.user.is_authenticated:
        return render(request,'admn/bookform.html')
    return redirect('frontpage')

@csrf_exempt
def added(request):
    if request.method == 'POST':
        try:
            bookid = request.POST['bookid']
            bookname = request.POST['bookname']
            writer = request.POST['writer']
            categ = request.POST['categ']
            isb = request.POST['isb']
            descp = request.POST['descp']
            img = request.FILES['img']
            if request.FILES.get('pdff'):
                pdff = request.FILES['pdff']
                l1= Book(Book_id=bookid,Book_Name=bookname,author=writer,category=categ,ISBN_10=isb,desc=descp,image=img,pdf=pdff)
                l1.save()
                l2= Part_2(Book_id=bookid,Book_Name=bookname,author=writer)
                l2.save()
                messages.success(request,'Book Added Successfully')
                return redirect('AddBook')
            else:
                l1= Book(Book_id=bookid,Book_Name=bookname,author=writer,category=categ,ISBN_10=isb,desc=descp,image=img)
                l1.save()
                l2= Part_2(Book_id=bookid,Book_Name=bookname,author=writer)
                l2.save()
                messages.success(request,'Book Added Successfully')
                return redirect('AddBook')
        except:
            messages.error(request,'All parts are necessary except pdf')
            return redirect('AddBook')
    return HttpResponse('Invalid')