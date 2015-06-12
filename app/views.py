from django.shortcuts import render, redirect
from app.models import Question, Answer
import random

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