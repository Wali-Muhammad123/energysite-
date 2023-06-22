from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError



# Views
def index(request):
    return render(request,"uwapp/index.html")


def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        content = Subscribe(email=email)
        content.save()
        messages.success(request,"Successfully Subscribed: Check your Email")
        return redirect('index')
    return render(request,"uwapp/index.html")


def contact(request):
    if request.method == "POST":
        fullname     = request.POST['fullname']
        house_number = request.POST['housenum']
        postcode = request.POST['postcode']
        telephone = request.POST['telnumber']
        email = request.POST['email']
        besttime = request.POST.getlist(u'besttime')
        services = request.POST.getlist(u'service')
        content = Contact(full_name=fullname,house_number=house_number,postcode=postcode,telephone=telephone,email=email,besttime=besttime,services=services)
        content.save()
        messages.success(request,"We have successfully received your quote request. Our representative will contact you in 24 hours.")
        # try:
        #     send_mail(f'Thank you for Subscribing', f'Hi,\n\nThank you for subscribing to BT Business Official Partner.\n\nIf you have any questions please feel free to contact us, we are just an email away.\n\nThank You\n\nCustomers Service.\nBT Business Partner UK',email, ['support@marketingservicesonline.co.uk'])
        # except BadHeaderError:
        #     return HttpResponse('Invalid header found.')
        # try:
        #     send_mail(f'Thank you for Subscribing', f'Hi,\n\nThank you for subscribing to BT Business Official Partner.\n\nIf you have any questions please feel free to contact us, we are just an email away.\n\nThank You\n\nCustomers Service.\nBT Business Partner UK', 'support@marketingservicesonline.co.uk',[email])
        # except BadHeaderError:
        #     return HttpResponse('Invalid header found.')
        return redirect('newsite')
    return render(request,"uwapp/index.html")


def newsite(request):
    return render(request,"uwapp/newsite/index.html")


def info(request):
    if request.method == "POST":
        name     = request.POST['name']
        phone = request.POST['phone']
        postcode = request.POST['postcode']
        email = request.POST['email']
        content_info = leads(name=name,phone=phone,postcode=postcode,email=email)
        content_info.save()
        return redirect('/')
    return redirect('/')

import csv
def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="All leads.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID','Name','Phone','Postcode','Emails'])
    users = leads.objects.all().values_list('id','name','phone','postcode','email')
    for user in users:
        writer.writerow(user)
    return response
