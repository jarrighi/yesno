from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	user = models.ForeignKey(User, null=True)
	question = models.TextField(max_length=1000, null=True)
	published = models.DateTimeField(auto_now_add=True, null=True)

	def __unicode__(self):
		# return "Question # {}".format(self.id)
		return str(self.question)

class Answer(models.Model):
	user = models.ForeignKey(User, null=True)
	question = models.ForeignKey(Question, null=True)
	published = models.DateTimeField(auto_now_add=True, null=True)
	answer = models.NullBooleanField()

	def __unicode__(self):
		return "Answer # {}".format(self.id)

class UserProfile(models.Model):
	HER = 'Her'
	HIM = 'Him'
	THEM = 'Them'

	GENDER_CHOICES = (
		(HER, 'Her'), 
		(HIM, 'Him'),
		(THEM, 'Them')
		)
	user = models.OneToOneField(User)
	birthdate = models.DateField()
	gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
	zipcode = models.CharField(max_length=10)

	def __unicode__(self):
		return "Profile # {}".format(self.id)



