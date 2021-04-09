from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request,'index.html',{})

def submit(request):
    if request.method == 'POST':
        time = request.POST.get('time','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        content=''' Subject : {0}
        Time : {1}
        Message : {2}'''.format(subject,time,message)

        send_mail(
            subject,
            content,
            'example@gmail.com',
            ['receiver1@gmail.com','receiver2@gmail.com','receiver3@gmail.com','receiver4@gmail.com'],
            )
        
        return render(request, 'index.html',{time:'time',message:'message',subject:'subject'})
        
    
    else:
        return render(request, 'index.html',{})

# Create your views here.
