from django.contrib import admin

from . import models
from .models import *

# Register your models here.
admin.site.register(Admin)
admin.site.register(Artist)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Products)
# admin.site.register(ArtistProfile)
# admin.site.register(CustomerProfile)


