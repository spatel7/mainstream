from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField("date created")
	users = models.ManyToManyField(User)

	def __unicode__(self):
		return self.name

	def get_streams(self):
		return self.stream_set.all()

class Stream(models.Model):
	group = models.ForeignKey(Group)
	user = models.ForeignKey(User)
	topic = models.CharField(max_length=200)
	date = models.DateTimeField("date created")

	def __unicode__(self):
		return self.topic

	def get_posts(self):
		return self.post_set.all()

class Post(models.Model):
	stream = models.ForeignKey(Stream)
	user = models.ForeignKey(User)
	content = models.CharField(max_length=200)
	date = models.DateTimeField("date created")

	def __unicode__(self):
		return self.content