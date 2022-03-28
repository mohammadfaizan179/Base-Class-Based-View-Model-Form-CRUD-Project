from django import forms
from django.db import models
from django.forms import fields, widgets
from enroll.models import Student_Model

class Student_Form(forms.ModelForm):
    class Meta:
        model = Student_Model
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Enter Name', 'class':'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'placeholder':'Enter Email', 'class':'form-control mb-3'}),
            'password': forms.PasswordInput(render_value=True, attrs={'placeholder':'Enter Password', 'class':'form-control mb-3'}),
        }