import uuid
from email import message
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import Artist, Customer  # Import your user models


from .models import *
from django.contrib import messages
#src
from django.shortcuts import render, redirect

from django.core.mail import send_mail
import random
from .models import *
from .utils import send_email_token


# Create your views here.
def adminhome(request):
    return render(request,"adminhome.html")
def logout(request):
    return render(request,"login.html")
def changepassword(request):
    return render(request,"changepassword.html")
def myhome(request):
    return render(request,"index.html")
def checkadminlogin(request):
    adminuname = request.POST["uname"]  # request .GET["uname"]
    adminpassword = request.POST["password"]  ##request.POST["password"]

    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpassword))
    print(flag)

    if flag:
        #request.session["auname"] = adminuname  # a this is called creating a session variable
        return render(request, "adminhome.html", {"uname": adminuname})  # return HttpResponse("Login success")
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"message": msg})

def home(request):
    return render(request,"index.html")
def paintings(request):
    return render(request,"paintings.html")
def sculptures(request):
    return render(request,"sculptures.html")
def checkartistlogin(request):
    artistuname = request.POST.get("artuname")
    artistpassword=request.POST.get("artpassword")
    flag2 = Artist.objects.filter(Q(username=artistuname) & Q(password=artistpassword))
    print(flag2)
    if flag2:
       request.session["auname"] = artistuname  # a this is called creating a session variable
       return render(request, "artisthome.html", {"artuname": artistuname})  # return HttpResponse("Login success")
    else:
        msg = "Login Failed"
        return render(request, "artistlogin.html", {"message": msg})


def checkcustomerlogin(request):
    customeruname = request.POST["customeruname"]
    customerpassword= request.POST["customerpassword"]
    flag1 = Customer.objects.filter(Q(username=customeruname) & Q(password=customerpassword))
    print(flag1)

    if flag1:
        request.session["auname"] = customeruname  # a this is called creating a session variable
        return render(request, "customerhome.html", {"customeruname": customeruname})  # return HttpResponse("Login success")
    else:
        msg = "Login Failed"
        return render(request, "customerlogin.html", {"message": msg})

# def register(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             adminuname = form.cleaned_data["uname"]
#             adminpassword = form.cleaned_data["password"]
#             admincategory = form.cleaned_data["user"]
#             adminemail = form.cleaned_data["email"]
#             adminphone = form.cleaned_data["phone"]
#             admingender = form.cleaned_data["gender"]
#             admincategory1 = form.cleaned_data["category"]
#
#             if admincategory == "Artist":
#                 artist = Artist(username=adminuname, password=adminpassword, email=adminemail, phonenumber=adminphone, gender=admingender)
#                 artist.save()
#                 return render(request, "artistlogin.html")
#             elif admincategory == "Customer":
#                 customer = Customer(username=adminuname, password=adminpassword, email=adminemail, phonenumber=adminphone, gender=admingender)
#                 customer.save()
#                 return render(request, "customerlogin.html")
#             else:
#                 message.error(request, "Invalid category Selection")
#                 return render(request, "login.html")
#     else:
#         form = RegistrationForm()
#
#     return render(request, "login.html", {"form": form})
def register(request, message=None):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpassword = request.POST["password"]
        admincategory = request.POST["user"]
        adminemail = request.POST["email"]
        adminphone = request.POST["phone"]
        admingender = request.POST["gender"]
        admincategory1 = request.POST["category"]

    if admincategory == "Artist":
        artist = Artist(username=adminuname, password=adminpassword, email=adminemail, phonenumber=adminphone,
                        gender=admingender)
        Artist.save(artist);
        return render(request, "artistlogin.html")
    elif admincategory == "Customer":
        customer = Customer(username=adminuname, password=adminpassword, email=adminemail, phonenumber=adminphone,
                            gender=admingender)
        Customer.save(customer);
        return render(request, "customerlogin.html")
    else:
        message.error(request, "Invalid category Selection")
        return render(request, "login.html")


#src
# def generate_otp():
#     return str(random.randint(1000, 9999))
#
# otp_storage = {}
#
# def send_otp_email(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         otp = generate_otp()
#
#
#         otp_storage[email] = otp
#
#         subject = 'OTP Verification'
#         message = f'Your OTP is: {otp}'
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [email]
#
#         send_mail(subject, message, from_email, recipient_list)
#
#         return render(request, 'validate_otp.html')
#     return render(request, 'send_otp.html')

# def validate_otp(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         user_otp = request.POST['otp']
#
#
#         stored_otp = otp_storage.get(email)
#
#         if user_otp == stored_otp:
#             return redirect('')
#         else:
#             return redirect('validate_otp',msg='InValid OTP')
#
#     return render(request, 'validate_otp.html')




def viewartists(request):
    auname = request.session["auname"]
    artist =Artist.objects.all()
    return render(request,"viewartists.html",{"artists":artist})

#def success(request):
 #   return render(request,"success.html")
#def token_send(request):
    #return render(request,"token_send.html")

'''
def homeee(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User(username = email)
        user_obj.set_password(password)
        Profile.objects.create(
            user = user_obj,
            email_token = str(uuid.uuid64())
        )
        send_email_token(email, p_obj.email_token)
    return render(request,"")

def verify(request,token):
    try:
        obj = Profile.objects.get(email_token = token)
        obj.is_verified = True
        obj.save()
        return HttpResponse("Your account is verified")

    except Exception as e:
      return HttpResponse("Invalid Login")
'''


# def force_text(param):
#     pass
#
#
# def email_verification(request, model_type, user_idb64, token):
#     try:
#         # Decode the user ID from base64
#         user_id = force_text(urlsafe_base64_decode(user_idb64))
#
#         # Find the user based on the model type
#         if model_type == "artist":
#             user = Artist.objects.get(pk=user_id)
#         elif model_type == "customer":
#             user = Customer.objects.get(pk=user_id)
#         else:
#             # Handle invalid model types
#             messages.error(request, "Invalid user type")
#             return render(request, "invalid_verification.html")
#
#         # Verify the token
#         if default_token_generator.check_token(user, token):
#             # Mark the user as verified (e.g., set a verified field to True)
#             user.verified = True
#             user.save()
#
#             # Redirect to a success page or login page
#             messages.success(request, "Email verified successfully. You can now log in.")
#             return redirect("login")  # Replace "login" with your actual login URL name
#         else:
#             messages.error(request, "Invalid token")
#             return render(request, "invalid_verification.html")
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         # Handle exceptions (e.g., user not found or invalid token)
#         messages.error(request, "Email verification failed")
#         return render(request, "invalid_verification.html")
def add_painting(request):
    auname = request.session["auname"]
    form = AddPaintingForm
    if request.method == 'POST':
         form1 = AddPaintingForm(request.POST,request.FILES)
         if form1.is_valid():
            form1.save()
            message ="Painting Added Successfully"
            return render(request,"addpainting.html",{"msg":message,"form":form})
         else:
             message = "Failed to Add Painting"
             return render(request,"addpainting.html",{"msg":message,"form":form})
    return render(request, "addpainting.html", {"form": form})

def oilpaintings(request):
    auname = request.session["auname"]
    products = Products.objects.filter(Q(category__name="OilPaintings"))
    return render(request,"oilpaintings.html",{'products':products})

def pencilpaintings(request):
    auname = request.session["auname"]
    products = Products.objects.filter(Q(category__name="PencilPaintings"))
    return render(request,'pencilpaintings.html',{'products':products})
def glasspaintings(request):
    auname = request.session["auname"]
    products = Products.objects.filter(Q(category__name="Glasspaintings"))
    return render(request,"glasspaintings.html",{'products':products})
def waterpaintings(request):
    auname = request.session["auname"]
    products = Products.objects.filter(Q(category__name="WaterPaintings"))
    return render(request,"waterpaintings.html",{'products':products})





# def add_painting(request):
#     form = AddPaintingForm
#     if request.method == 'POST':
#         form1 = AddPaintingForm(request.POST)
#         if form1.is_valid():
#             form1.save()
#             message ="Painting Added Successfully"
#             return render(request,"addpainting.html",{"msg":message,"form":form})
#         else:
#             message = "Failed to Add Painting"
#             return render(request,"addpainting.html",{"msg":message,"form":form})
#     return render(request, "addpainting.html", {"form": form})

def carvedsculptures(request):
    auname = request.session["auname"]
    products = Products.objects.all()
    return render(request,"carvedsculptures.html",{'products':products})
def modeledsculptures(request):
    auname = request.session["auname"]
    products = Products.objects.all()
    return render(request,"modeledsculptures.html",{'products':products})
def assembledsculptures(request):
    auname = request.session["auname"]
    products = Products.objects.all()
    return render(request,"assembledsculptures.html",{'products':products})
def reliefsculptures(request):
    auname = request.session["auname"]
    products = Products.objects.all()
    return render(request,"reliefsculptures.html",{'products':products})

def add_sculpture(request):
    auname = request.session["auname"]
    form = AddSculptureForm
    if request.method == 'POST':
        form1 = AddPaintingForm(request.POST)
        if form1.is_valid():
            form1.save()
            message ="Sculpture Added Successfully"
            return render(request,"addsculpture.html",{"msg":message,"form":form})
        else:
            message = "Failed to Add Sculpture"
            return render(request,"addsculpture.html",{"msg":message,"form":form})
    return render(request, "addsculpture.html", {"form": form})

