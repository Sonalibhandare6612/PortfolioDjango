from django.shortcuts import render, HttpResponse
from myapp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def intro(request):
    return render(request,'intro.html')

def education(request):
    return render(request,'edu.html')

def project(request):
    return render(request,'project.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        enquiry = request.POST['enquiry']
        ins = Contact(name=name, email=email, phone=phone, enquiry=enquiry)
        ins.save()
        return render(request,'contact.html')
    return render(request,'contact.html')
