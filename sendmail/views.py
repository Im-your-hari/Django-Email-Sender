from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Student


def index(request):
    return render(request,'index.html',{})

def submit(request):
    obj = Student.objects.all()
    

    mail_list = []
    for i in obj:
        print(i.email)
        mail_list.append(i.email)
        print(mail_list)
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
            mail_list,
            )
        
        return render(request, 'index.html',{time:'time',message:'message',subject:'subject'})
        
    
    else:
        return render(request, 'index.html',{})

# Create your views here.
