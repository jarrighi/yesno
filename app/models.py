from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	user = models.ForeignKey(User, null=True)
	question = models.TextField(max_length=1000, null=True)
	published = models.DateTimeField(auto_now_add=True, null=True)

	def __unicode__(self):
		# return "Question # {}".format(self.id)
		return self.question

class Answer(models.Model):
	user = models.ForeignKey(User, null=True)
	question = models.ForeignKey(Question, null=True)
	published = models.DateTimeField(auto_now_add=True, null=True)
	answer = models.NullBooleanField()

	def __unicode__(self):
		return "Answer # {}".format(self.id)


