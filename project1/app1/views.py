from django.shortcuts import render,redirect
from django.http import HttpResponse
from . form import EmployeeForm
from . models import Employee


from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # form.save()
            email = form.cleaned_data['name']
            a = form.cleaned_data['age']
            sql = Employee(name=email,age=a)
            sql.save()


            subject = 'welcome to abc'
            message = f'Hi {email}, thank you for registering in abc.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )



            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
