from django.shortcuts import render, redirect
from app.models import Question, Answer
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


def question(request):
	# questions = Question.objects.order_by('published')

	try:
		qid = int(request.GET.get("p"))
	except:
		maxid = Question.objects.latest('id').id
		qid = random.randint(1, maxid)
	question = Question.objects.get(id=qid) 
	text = 	question.question
	print(text)
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
	