from django import forms
from .models import *
from django import forms
from django.core.exceptions import ValidationError


class AddPaintingForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        labels = {
            "name": "Name of Painting",
            "price": "Set Your Price",
            "category": "Category of the Painting",
            "description": "Description of the Painting",
            "image": "Upload the Image",
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }

class AddSculptureForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        labels = {
            "name": "Name of Sculpture",
            "price": "Set Your Price",
            "category": "Category of the Sculpture",
            "description": "Description of the Painting",
            "image": "Upload the Image",
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }

#
# class ArtistProfileForm(forms.ModelForm):
#     class Meta:
#         model = ArtistProfile
#         fields = "__all__"
#         labels = {
#             "artistname": "Name of the Artist",
#             "artistbio": "Enter Your Bio",
#         }
#
#         widgets = {
#             "artistname": forms.TextInput(attrs={"class": "form-control"}),
#             "artistbio": forms.Textarea(attrs={"class": "form-control"}),
#         }


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    user = forms.ChoiceField(choices=[("Artist", "Artist"), ("Customer", "Customer")])
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    category = forms.ChoiceField(choices=[("Category1", "Category1"), ("Category2", "Category2")])

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email field is required.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise ValidationError("Phone field is required.")
        # Add additional phone number validation here if needed
        return phone
