from django.db.models import Q
from django.shortcuts import render

#src
from django.core.mail import send_mail
import random

from artproject.artproject import settings


def generate_otp():
    return str(random.randint(1000, 9999))

otp_storage = {}

def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generate_otp()


        otp_storage[email] = otp

        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'validate_otp.html')
    return render(request, 'send_otp.html')

def validate_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_otp = request.POST['otp']


        stored_otp = otp_storage.get(email)

        if user_otp == stored_otp:

            return redirect('attendance_list')
        else:
            return redirect('validate_otp',msg='InValid OTP')

    return render(request, 'validate_otp.html')



# Create your views here.
