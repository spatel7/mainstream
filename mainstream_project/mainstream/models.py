from django.db import models

class Group(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField("date created")

	def __unicode__(self):
		return self.name

	def get_streams(self):
		return self.stream_set.all()

class Stream(models.Model):
	group = models.ForeignKey(Group)
	author = models.CharField(max_length=200)
	topic = models.CharField(max_length=200)
	date = models.DateTimeField("date created")

	def __unicode__(self):
		return self.topic

	def get_posts(self):
		return self.post_set.all()

class Post(models.Model):
	stream = models.ForeignKey(Stream)
	author = models.CharField(max_length=200)
	content = models.CharField(max_length=200)
	date = models.DateTimeField("date created")

	def __unicode__(self):
		return self.content