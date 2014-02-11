import os
from django.utils import timezone

def populate():
	g1 = add_group("Highschool Friends")
	g2 = add_group("Davidson 710")

	s1 = add_stream(g1, "Sahil", "Why don't athletes get paid less?")

	add_post(stream=s1,
		author="Sahil",
		content="I mean, it honestly is quite a bit of money right?")

	add_post(stream=s1,
		author="Shoham",
		content="Yeah but they risk their lives everyday to entertain millions.")

	add_post(stream=s1,
		author="Senthil",
		content="I feel they should be paid even more than they are now.")

	s2 = add_stream(g1, "Senthil", "Best moment of highschool")

	add_post(stream=s2,
		author="Senthil",
		content="What do you guys feel was the best part of our highschool?")

	add_post(stream=s2,
		author="Sahil",
		content="Obviously us!")

	for group in Group.objects.all():
		for stream in Stream.objects.filter(group=group):
			for post in Post.objects.filter(stream=stream):
				print "- {0} - {1} - {2}".format(str(group), str(stream), str(post))

def add_group(name):
	g = Group.objects.get_or_create(name=name, date=timezone.now())[0]
	return g

def add_stream(group, author, topic):
	s = Stream.objects.get_or_create(group=group, author=author, topic=topic, date=timezone.now())[0]
	return s

def add_post(stream, author, content):
	p = Post.objects.get_or_create(stream=stream, author=author, content=content, date=timezone.now())[0]
	return p

if __name__ == '__main__':
	print "Starting Mainstream population"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainstream_project.settings')
	from mainstream.models import Group, Stream, Post
	populate()