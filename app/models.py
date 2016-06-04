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

	class Meta:
		unique_together = (('user', 'question'),)

	def __unicode__(self):
		return "Answer # {}".format(self.id)

class UserProfile(models.Model):

	GENDER_CHOICES = (
		('Her', 'Her'), 
		('Him', 'Him'),
		('Them', 'Them')
		)

	INCOME_CHOICES = (
		('a', '$0-$35,000'),
		('b', '$35,001-$50,000'),
		('c', '$50,001-$100,000'),
		('d', '$100,001+')
		)

	RACE_CHOICES = (
		('Asian', 'Asian'),
		('Middle Eastern', 'Middle Eastern'),
		('Black', 'Black'),
		('Native American', 'Native American'),
		('Hispanic/Latin', 'Hispanic/Latin'),
		('Pacific Islander', 'Pacific Islander'),
		('White', 'White'),
		('Mixed', 'Mixed'),
		('Other', 'Other')
		)
		
	ORIENTATION_CHOICES = (
		('Men', 'Men'),
		('Women', 'Women'),
		('Everyone', 'Everyone'),
		('Neither', 'Neither'),
		('Other', 'Other')
		)

	user = models.OneToOneField(User)
	birthdate = models.DateField()
	gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
	zipcode = models.CharField(max_length=10)
	income = models.CharField(max_length=1, choices=INCOME_CHOICES, blank=True, null=True)
	race = models.CharField(max_length=15, choices=RACE_CHOICES, blank=True, null=True)
	orientation = models.CharField(max_length=15, choices=ORIENTATION_CHOICES, blank=True, null=True)

	def __unicode__(self):
		return "{}'s Profile".format(self.user.username)



