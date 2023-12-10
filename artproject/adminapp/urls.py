from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome"),
    path("adminlogout",views.logout,name="adminlogout"),
    path("changepassword",views.changepassword,name="changepassword"),
    path("myhome",views.myhome,name="myhome"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("register",views.register,name="register"),
    path("",views.home,name=""),
    path("paintings",views.paintings,name="paintings"),
    path("sculptures", views.sculptures, name="sculptures"),
    path("viewartists", views.viewartists, name="viewartists"),
    path("checkartistlogin",views.checkartistlogin,name="checkartistlogin"),
    path("checkcustomerlogin",views.checkcustomerlogin,name="checkcustomerlogin"),
    #path("send_otp_email",views.send_otp_email,name="send_otp_email"),
    #path("generate_otp",views.generate_otp,name="generate_otp"),
    #path("validate_otp",views.validate_otp,name="validate_otp"),
    #path("token_send",views.token_send,name="token_send"),
   # path("success",views.success,name="success"),
   # path("homeee",views.homeee,name="homee"),
   # path("verify",views.verify,name="verify"),
    #path('email-verification/<str:model_type>/<str:token>/', views.email_verification, name='email_verification'),
    path("oilpaintings",views.oilpaintings,name="oilpaintings"),
    path("pencilpaintings",views.pencilpaintings,name="pencilpaintings"),
    path("glasspaintings",views.glasspaintings,name="glasspaintings"),
    path("waterpaintings",views.waterpaintings,name="waterpaintings"),
     path("add_painting",views.add_painting,name="add_painting"),
    path("carvedsculptures",views.carvedsculptures,name="carvedsculptures"),
    path("modeledsculptures", views.modeledsculptures, name="modeledsculptures"),
    path("reliefsculptures", views.reliefsculptures, name="reliefsculptures"),
    path("assembledsculptures", views.assembledsculptures, name="assembledsculptures"),
path("add_sculpture",views.add_sculpture,name="add_sculpture"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)