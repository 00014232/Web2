from django.forms import forms
from django.http.response import BadHeaderError
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def home(request):
    return render(request, "Asosiy/home.html")
def about(request):
    return render(request, "Haqimizda/about.html")
def courses(request):
    return render(request, "Kurslar/courses.html")
def galery(request):
    return render(request,"Galereya/galery.html")
def more(request):
    return render(request, "Ko'proq/more.html")
def prices(request):
    return render(request, "Narxlar/prices.html")
def contacts(request):
    return render(request, "Aloqa/contact.html")
def successView():
    return HttpResponse(' Muvaffaqiyatli ! Xabar qoldirganingiz uchun raxmat. ')

