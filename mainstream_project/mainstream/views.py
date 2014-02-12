from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from mainstream.models import Group, Stream, Post
from mainstream.forms import GroupForm
from django.utils import timezone

def index(request):
	context = RequestContext(request)
	context_dict = {}
	context_dict['groups'] = Group.objects.all()
	context_dict['streams'] = Stream.objects.all()
	context_dict['posts'] = Post.objects.all()
	return render_to_response("mainstream/index.html", context_dict, context)

def group(request, group_id_url):
	context = RequestContext(request)
	group_id = group_id_url
	context_dict = {'group_id': group_id}
	try:
		group = Group.objects.get(id=group_id)
		streams = Stream.objects.filter(group=group)
		context_dict['streams'] = streams
		context_dict['group'] = group
	except Group.DoesNotExist:
		pass
	return render_to_response("mainstream/group.html", context_dict, context)

def add_group(request):
	context = RequestContext(request)
	if request.method == 'POST':
		group_form = GroupForm(request.POST)
		if group_form.is_valid():
			group = group_form.save(commit=False)
			group.date = timezone.now()
			group.save()
			return HttpResponseRedirect("/mainstream/")
		else:
			print group_form.errors
	else:
		group_form = GroupForm
	return render_to_response("mainstream/add_group.html", {'group_form': group_form}, context)