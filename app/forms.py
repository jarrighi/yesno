from django import forms
from app.models import User, Question, UserProfile

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


class UserProfileForm(forms.ModelForm):
  
  GENDER_CHOICES = (
    ('Her', 'Her'), 
    ('Him', 'Him'),
    ('Them', 'Them')
    )

  INCOME_CHOICES = (
    ('a', '$0-$35,000'),
    ('b', '$35,001-$50,000'),
    ('c', '$50,001-$100,000'),
    ('d', '$100,001+')
    )

  RACE_CHOICES = (
    ('Asian', 'Asian'),
    ('Middle Eastern', 'Middle Eastern'),
    ('Black', 'Black'),
    ('Native American', 'Native American'),
    ('Hispanic/Latin', 'Hispanic/Latin'),
    ('Pacific Islander', 'Pacific Islander'),
    ('White', 'White'),
    ('Mixed', 'Mixed'),
    ('Other', 'Other')
    )
    
  ORIENTATION_CHOICES = (
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Everyone', 'Everyone'),
    ('Neither', 'Neither'),
    ('Other', 'Other')
    )

  birthdate = forms.DateField(help_text="What date were you born?",
                              widget=forms.DateInput, 
                              required=True)
  gender = forms.ChoiceField(help_text="Select your pronoun", 
                              choices=GENDER_CHOICES,
                              required=True)
  zipcode = forms.CharField(help_text="What's your zipcode?", 
                              required=True)
  income = forms.ChoiceField(help_text="How much do you make?", 
                              choices=INCOME_CHOICES)
  race = forms.ChoiceField(help_text="What's your race?", 
                              choices=RACE_CHOICES)
  orientation = forms.ChoiceField(help_text="Who are you attracted to?", 
                              choices=ORIENTATION_CHOICES)

  class Meta:
    # Provide an association between the ModelForm and a model
    model = UserProfile
    fields = ('birthdate', 'gender', 'zipcode', 'income', 'race', 'orientation')



class QuestionForm(forms.ModelForm):
  question = forms.CharField(help_text="Write a yes/no question.",
                              min_length=12,
                              max_length=500,
                              required=True)
 # user = forms.IntegerField(widget=forms.HiddenInput())
  def save(self, user, commit=True):
    # Save the provided password in hashed format
    question = super(QuestionForm, self).save(commit=False)
    question.user = user
    if commit:
      question.save()


  class Meta:

    model = Question
    fields = ('question',)
  
    