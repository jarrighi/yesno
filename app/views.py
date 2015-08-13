from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from app.models import Question, Answer
from django.contrib.auth.models import User
import random
import json


def question(request):
  #get all questions as array
	questions = Question.objects.order_by('published') 
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

def submit(request):
 	if request.method =='POST':
 		print request.POST

 	return render(request, 'app/submit.html')
 	# context_dict = {}
 	# return render(request, 'app/submit.html', context_dict)

@csrf_exempt
def submit_ajax(request):
 	if request.method == 'POST':
		
 		question_text = request.POST.get("question_text")
 		question_data = {}
 		question = Question(question=question_text)
 		question.save()

 		question_data['results'] = 'Your question has been submitted'
 		question_data['question'] = question.question
 		question_data['published'] = question.published.strftime('%B %d, %Y %I:%M %p')

 		return HttpResponse( 
             json.dumps(question_data),
             content_type="application/json"
         )
 	else:
 		return HttpResponse(
             json.dumps({"nothing to see": "this isn't happening"}),
             content_type="application/json"
         )
	
def signup(request):
    if request.method == "POST":
        User.objects.create_user(request.POST["username"], None, request.POST["password"])
    return render(request, 'app/signup.html')