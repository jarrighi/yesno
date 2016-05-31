from django.shortcuts import render, redirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from app.models import Question, Answer, UserProfile
from app.forms import UserForm, QuestionForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random
import json

@login_required(login_url='/login')
def question(request):
  uid = request.user.id
  # get one random question the current user has not answered
  try: 
    question = Question.objects.exclude(answer__user=uid).order_by('?')[0]
  except IndexError:
    return render(request, 'app/index.html')
  return render(request, 'app/index.html', {'question': question})


def answer_ajax(request, qid, choice):
  #Add the users answer to the DB
  choice = True if choice == 'yes' else False
  q = Question.objects.get(id=qid)
  a = Answer(question = q, answer = choice, user=request.user)
  a.save()

  # Get answer data to send back to user
  response_content = {}
  yesses = Answer.objects.filter(question=qid, answer=True).count()
  response_content['yesses'] = yesses
  nos = Answer.objects.filter(question=qid, answer=False).count()
  response_content['nos'] = nos
  
  return HttpResponse(
            json.dumps(response_content), 
            content_type="application/json"
            )

@login_required(login_url='/login')
def submit_q(request):
  if request.method =='POST':
    form = QuestionForm(request.POST)
    if form.is_valid():
      form.save(request.user)
      messages.add_message(request, messages.SUCCESS, "Thanks for submitting a question")
      return HttpResponseRedirect(reverse('submit_q'))
    else:
      print form.errors
  else:
    form = QuestionForm()

  return render(request, 'app/submit.html', {'form': form})
 	
	
def signup(request):
  if request.method == "POST":
    userform = UserForm(request.POST)
    profileform = UserProfileForm(request.POST)
    if userform.is_valid() and profileform.is_valid():
      user = userform.save()
      print user
      profile = profileform.save(commit=False)
      profile.user = user
      profile.save()

      return question(request)
    else:
        # The supplied form contained errors - just print them to the terminal.
      print userform.errors, profileform.errors
  else:
      # If the request was not a POST, display the form to enter details.
    userform = UserForm()
    profileform = UserProfileForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
  return render(request, 'app/signup.html', 
                  {'userform': userform, 'profileform': profileform})
  

def loginview(request):
  if request.method == "POST":
    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
    # the password verified for the user
      if user.is_active:
        print "User is valid, active and authenticated"
        login(request, user)
        return redirect('/')
      else:
        print "The password is valid, but the account has been disabled!"
    else:
        # the authentication system was unable to verify the username and password
      print "The username and password were incorrect."

  return render(request, 'app/login.html')

def logoutview(request):
  logout(request)
  return render(request, 'app/login.html')

@login_required(login_url='/login')
def profile(request):
  question_list = Question.objects.filter(user=request.user.id)
  answer_list = Question.objects.filter(answer__user=request.user.id)
  profile = UserProfile.objects.get(user_id=request.user.id)
  return render(request, 'app/profile.html', 
                  {'question_list': question_list, 'answer_list': answer_list, 'profile': profile})







