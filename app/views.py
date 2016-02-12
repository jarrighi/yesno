from django.shortcuts import render, redirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from app.models import Question, Answer
from app.forms import UserForm, QuestionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random
import json

@login_required(login_url='/login')
def question(request):
  #get all questions as array
	questions = Question.objects.exclude(question=None).order_by('published') 
  #randomly choose question from query results. This is an int.
	q_index = random.randint(0, len(questions)-1) 
  #question object from questions array
	chosen_question = questions[q_index]
  #string containing the question 
	text = 	chosen_question.question 

	print(text)
	qid = chosen_question.id
	return render(request, 'app/index.html', {'question': text, 'qid': qid})


def answer_ajax(request, qid, choice):
  #Add the users answer to the DB
  choice = True if choice == 'yes' else False
  q = Question.objects.get(id=qid)
  a = Answer(question = q, answer = choice)
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

def submit_q(request):
  if request.method =='POST':
    form = QuestionForm(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, "Thanks for submitting a question")
      return HttpResponseRedirect(reverse('submit_q'))
    else:
      print form.errors
  else:
    form = QuestionForm()

  return render(request, 'app/submit.html', {'form': form})
 	
	
def signup(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return question(request)
    else:
        # The supplied form contained errors - just print them to the terminal.
      print form.errors
  else:
      # If the request was not a POST, display the form to enter details.
    form = UserForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
  return render(request, 'app/signup.html', {'form': form})
  

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
