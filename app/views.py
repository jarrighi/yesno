from django.shortcuts import render, redirect
from app.models import Question

def question(request):
	# questions = Question.objects.order_by('published')
	try:
		qid = int(request.GET.get("p"))
	except:
		qid = 1 
	question = Question.objects.get(id=qid) 
	text = 	question.question
	# qid = question.id
	nextid = qid + 1
	lastid = qid - 1
	print(text)
	return render(request, 'app/index.html', {'question': text, 'qid': qid, 'nextid': nextid, 'lastid': lastid})


def answer(request, *args):
	print "answered"
	return redirect('/')
