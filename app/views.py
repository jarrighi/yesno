from django.shortcuts import render, redirect
from app.models import Question, Answer
import random

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
	context_dict = {}
	return render(request, 'app/submit.html', context_dict)

@csrf_exempt
def submit_ajax(request):
	if request.method == 'POST':
		question = Question()
		question.question = request.POST.get("question_text")
		question.save()

		return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
	