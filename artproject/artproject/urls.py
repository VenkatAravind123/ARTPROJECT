"""
URL configuration for artproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
   path("admin/",admin.site.urls),
   path("",views.home,name=""),
   path("home1",views.home1,name="home1"),
   path("paintings",views.paintings,name="paintings"),
   path("sculptures", views.sculptures, name="sculptures"),
   path("artists", views.artists, name="artists"),
   path("about", views.about, name="about"),
   path("contact", views.contact, name="contact"),
   path("login",views.login,name="login"),
   path("signin",views.signin,name="signin"),
   path("artistlogin", views.artistlogin, name="artistlogin"),
   path("customerlogin", views.customerlogin, name="customerlogin"),
   #path("checkartistlogin")
   path("",include("adminapp.urls")),
   #path("",include("artistapp.urls")),
   #path("",include("customerapp.urls")),
   #for payment src
   path("",include("payments.urls")),
   path('cart/',include('cart.urls')),
]
