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

  def clean_password2(self):
    pass1 = self.cleaned_data.get('password1')
    pass2 = self.cleaned_data.get('password2')
    if pass1 and pass2 and pass1 != pass2:
      raise forms.ValidationError("Passwords don't match")
    return pass2

  def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('Email already used.')
        return email
  
  def save(self, commit=True):
    # Save the provided password in hashed format
    user = super(UserForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
      user.save()
    return user

  class Meta:
    # Provide an association between the ModelForm and a model
    model = User
    fields = ('username', 'email')