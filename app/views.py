from django.shortcuts import render, redirect
from app.models import Question, Answer
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


def question(request):
	questions = Question.objects.order_by('published') #get all questions as array
	q_index = random.randint(0, len(questions)-1) #randomly choose question from query results. This is an int.
	chosen_question = questions[q_index] #question object from questions array
	text = 	chosen_question.question #string containing the question

	print(text)
	qid = chosen_question.id
	return render(request, 'app/index.html', {'question': text, 'qid': qid})


def answer(request, qid, answer, *args):
	print(qid)
	print(answer)
	answermap = {'yes': True, 'no': False}
	answer = answermap[answer]
	print answer
	q = Question.objects.get(id=qid)
	a = Answer(question = q, answer = answer)
	a.save()
	return redirect('/')

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
	
