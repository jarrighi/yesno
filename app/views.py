from django.shortcuts import render, redirect
from app.models import Question
import random

def question(request):
	# questions = Question.objects.order_by('published')

	try:
		qid = int(request.GET.get("p"))
	except:
		maxid = Question.objects.latest('id').id
		print(maxid)
		qid = random.randint(1, maxid)
	question = Question.objects.get(id=qid) 
	text = 	question.question
	print(text)
	return render(request, 'app/index.html', {'question': text, 'qid': qid})


def answer(request, *args):
	print("answered")
	return redirect('/')
