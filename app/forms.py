from django import forms
from app.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField(min_length=5, max_length=16, required=True, 
					help_text="Choose your Ninja name (must be at least 5 characters long)")
	email = forms.EmailField(required=True, help_text="Enter your email address")
	password = forms.CharField(min_length=8, max_length=32, widget=forms.PasswordInput, required=True,
					help_text="Create your secret password- greater than 7 characters")

	class Meta:
        # Provide an association between the ModelForm and a model
	   model = User
	   fields = ('username', 'email', 'password')