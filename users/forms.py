from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=65,widget=forms.TextInput(
        attrs={
            'placeholder':'Enter your username',
            'class':'px-6 py-4 w-full border border-solid border-gray-600 rounded-lg mb-2'
        }
    ))
    password=forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password',
        'class':'px-6 py-4 w-full border border-solid border-gray-600 rounded-lg mb-4'
    }))

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','username','password1','password2']
        def clean_password(self):
            cd=self.cleaned_data
            if cd['password1']!=cd['password2']:
                raise forms.ValidationError('Password did not match')
            return cd['password2']
        
        def clean_email(self):
            data=self.cleaned_data['email']
            qs=User.objects.exclude(id=self.instance.id).filter(email=data)
            if qs.exists():
                raise forms.ValidationError('Email Already in Use')
            return data

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter your Username',
        'class':'px-6 py-4 w-full border border-solid border-gray-600 rounded-lg mb-2'
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter email address',
        'class':'px-6 py-4 w-full border border-solid border-gray-600 rounded-lg mb-2'
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password',
        'class':'px-6 py-4 w-full border border-solid border-gray-600 rounded-lg mb-2'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password',
        'class':'px-6 py-4 w-full border border-solid border-gray-600 rounded-lg mb-2'
    }))

        


        