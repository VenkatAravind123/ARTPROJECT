from django.urls import path
from . import views

urlpatterns = [
    path('payindex', views.payindex, name='payindex'),
]