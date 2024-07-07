from django import forms
from django.forms import ModelForm
from .models import Register_names, Registers


class Register_form(forms.ModelForm):

    class Meta:
        model = Register_names
        fields = ('name','email','password','conform_password')

class Register(forms.ModelForm):

    class Meta:
        model = Registers
        fields = ('name','email','password','conform_password')

class Customer_login(forms.ModelForm):
    class Meta:
        model = Registers
        fields = ('email', 'password')