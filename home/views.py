from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'variable': "This is Sent" 
    }
    return render(request,'index.html',context)
    # return HttpResponse('This is Homepage')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        description=request.POST.get('description')

        if len(name) == 0:
            messages.success(request, 'Name Required.!')
        elif len(email) == 0:
            messages.success(request, 'Email Required.!')
        elif len(mobile) == 0:
            messages.success(request, 'Contact No. Required.!')
        else:
            contact=Contact(name=name, email=email, mobile=mobile, description=description,date=datetime.today())
            contact.save()
            messages.success(request, 'Sent Successfully.!')
    return render(request,'contact.html')