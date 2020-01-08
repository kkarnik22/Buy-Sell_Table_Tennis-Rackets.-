from xml.dom.minidom import Text

from django import forms
from .models import *
from django.core import validators


class ImageForm(forms.ModelForm):
    class Meta:
        model = Racket
        fields = ('name_seller', 'email', 'username', 'address', 'name_bat', 'model_no', 'desc', 'price', 'date_make', 'photo')

        labels = {
            'name_seller': 'Name of the seller',
            'email': 'Email Address',
            'username': 'Your Username',
            'address': 'Address of the seller',
            'name_bat': 'Company name of the bat',
            'model_no': 'Model number of the bat',
            'desc': 'Description about the product',
            'price': 'Original Price Of the bat',
            'date_make': 'When did you buy it?',
            'photo': 'Upload an image'
        }

        widgets = {
            'name_seller': forms.TextInput(
                attrs={'class': 'input', 'required': True, 'autofocus': True, 'placeholder': 'Your name',
                       'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}),
            'email': forms.TextInput(
                attrs={'class': 'input', 'required': True, 'autofocus': True, 'placeholder': 'Enter the email where you wish yo receive mails'}),
            'username': forms.TextInput(attrs={'class': 'input', 'required': True, 'placeholder': 'To see your products, add your username'}),
            'address': forms.TextInput(
                attrs={'class': 'input', 'required': True, 'autofocus': True, 'placeholder': 'Where we can find you?'}),
            'name_bat': forms.TextInput(
                attrs={'class': 'input', 'required': True, 'autofocus': True, 'placeholder': 'eg@GKI,Jumbo',
                       'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}),
            'desc': forms.TextInput(attrs={'class': 'input', 'required': True, 'placeholder': 'Info'}),
            'model_no': forms.TextInput(attrs={'class': 'input', 'required': True, 'placeholder': 'Model No'}),
            'price': forms.TextInput(attrs={'class': 'input', 'required': True, 'placeholder': 'Price'}),
            'date_make': forms.TextInput(attrs={'class': 'input', 'required': True, 'placeholder': 'YEAR-MONTH-DAY'})
        }
