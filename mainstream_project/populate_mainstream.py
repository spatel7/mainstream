import os
from django.utils import timezone

def populate():
	u1 = add_user("spatel7", "123")
	u2 = add_user("dasmonster", "123")
	u3 = add_user("senth", "123")

	g1 = add_group("Highschool Friends", u1)
	g2 = add_group("Davidson 710", u1)

	add_user_to_group(g1, u2)
	add_user_to_group(g1, u3)
	add_user_to_group(g2, u2)
	add_user_to_group(g2, u3)

	s1 = add_stream(g1, u1, "Why don't athletes get paid less?")

	add_post(stream=s1,
		user=u1,
		content="I mean, it honestly is quite a bit of money right?")

	add_post(stream=s1,
		user=u2,
		content="Yeah but they risk their lives everyday to entertain millions.")

	add_post(stream=s1,
		user=u3,
		content="I feel they should be paid even more than they are now.")

	s2 = add_stream(g1, u3, "Best moment of highschool")

	add_post(stream=s2,
		user=u3,
		content="What do you guys feel was the best part of our highschool?")

	add_post(stream=s2,
		user=u1,
		content="Obviously us!")

	for group in Group.objects.all():
		for stream in Stream.objects.filter(group=group):
			for post in Post.objects.filter(stream=stream):
				print "- {0} - {1} - {2}".format(str(group), str(stream), str(post))

def add_user(username, password):
	u = User.objects.get_or_create(username=username)[0]
	u.set_password(password)
	u.save()
	return u

def add_group(name, user):
	g = Group.objects.get_or_create(name=name, date=timezone.now())[0]
	g.users.add(user)
	g.save()
	return g

def add_user_to_group(group, user):
	group.users.add(user)
	group.save()

def add_stream(group, user, topic):
	s = Stream.objects.get_or_create(group=group, user=user, topic=topic, date=timezone.now())[0]
	return s

def add_post(stream, user, content):
	p = Post.objects.get_or_create(stream=stream, user=user, content=content, date=timezone.now())[0]
	return p

if __name__ == '__main__':
	print "Starting Mainstream population"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainstream_project.settings')
	from mainstream.models import Group, Stream, Post
	from django.contrib.auth.models import User
	populate()