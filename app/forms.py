from django import forms
from app.models import User

class UserForm(forms.ModelForm):
  username = forms.CharField(help_text="Choose your Ninja name (must be at least 5 characters long)",
                              min_length=5, 
                              max_length=16, 
                              required=True)

  email = forms.EmailField(help_text="Enter your email address",
                              required=True)

  password1 = forms.CharField(help_text="Create your secret password- greater than 7 characters",
                              min_length=8, 
                              max_length=32, 
                              widget=forms.PasswordInput, 
                              required=True)

  password2 = forms.CharField(help_text="Confirm your password",
                              min_length=8, 
                              max_length=32, 
                              widget=forms.PasswordInput, 
                              required=True)

  class Meta:
    # Provide an association between the ModelForm and a model
    model = User
    fields = ('username', 'email')