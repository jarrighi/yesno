from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Question, Answer
import random
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

def answer_tallies(request, qid):
	response_content = {}

	yesses = Answer.objects.filter(question=qid, answer=True).count()
	response_content['yesses'] = yesses

	nos = Answer.objects.filter(question=qid, answer=False).count()
	response_content['nos'] = nos
	
	return HttpResponse(json.dumps(response_content), content_type="application/json")