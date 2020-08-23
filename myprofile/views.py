from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    if request.method == 'POST':

        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
            
        

        return render(request, "myprofile/home.html", {'name': name})

    else:
        return render(request, "myprofile/home.html", {})


    
    

def noPage(request):
  return render(request, 'myprofile/NoPage.html' )


def successView(request):
    return HttpResponse('Success! Thank you for your message.')