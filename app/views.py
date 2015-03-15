from django.shortcuts import render
from app.models import Question

def question(request):
	questions = Question.objects.order_by('published')
	print(questions)
	return render(request, 'app/index.html', {'questions': questions})



