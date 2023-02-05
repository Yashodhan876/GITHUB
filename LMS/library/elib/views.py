from django.conf import settings
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from admn.models import Part_2,Part_3,Part_4
import os

# Create your views here.
# def frontpage(request):
#     return HttpResponse("Hello")

def userpage(request):
    if request.user.is_authenticated:
        l1= Part_4.objects.filter(applicantname=request.user)
        l2= Book.objects.all()
        n=len(l1)
        params = {'Book':l2,'Hist':l1,'range':range(1,n)}
        return render(request, 'elib/userpage.html',params)
    return redirect('frontpage')

def AllBooks(request):
    if request.user.is_authenticated:
        Books = Book.objects.all()
        n=len(Books)
        params = {'Book':Books,'range':range(1,n)}
        return render(request, 'elib/AllBooks.html',params)
    return redirect('frontpage')

def cat(request,slug):
    if request.user.is_authenticated:
        l=['Science and Mathematics','History','Economics and Business','Electronics and Digital World','Literature and Fiction','Geography and Outer World']
        Books = Book.objects.filter(category=l[int(slug)])
        n=len(Books)
        params = {'Book':Books,'range':range(1,n)}
        return render(request, 'elib/AllBooks.html',params)
    return redirect('frontpage')

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.author.lower() or query in item.Book_Name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    if request.user.is_authenticated:
        query = request.GET.get('search')
        Books = Book.objects.all()
        prod = [item for item in Books if searchMatch(query.lower(), item)]
        n=len(prod)
        params = {'Book':prod,'range':range(1,n)}
        if len(prod) == 0 or len(query)<4:
            messages.error(request,'Invalid Search / Book Not Found')
            return render(request, 'elib/search.html',params)
        return render(request, 'elib/search.html',params)
    return redirect('frontpage')

def Apply(request, slug):
    if request.user.is_authenticated:
        try:
            l1= Part_2.objects.get(Book_id=int(slug))
            l2= Part_3(Book_id=l1.Book_id,Book_Name=l1.Book_Name,author=l1.author,applicantname=request.user)
            l2.save()
            l1.delete()
            messages.success(request,'Applied for the Book Successfully')
            return redirect('userpage')
        except:
            messages.error(request,'Book is Not Available')
            return redirect('userpage')
    return redirect('frontpage')  


    