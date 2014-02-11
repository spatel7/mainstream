from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from mainstream.models import Group, Stream, Post

def index(request):
	context = RequestContext(request)
	context_dict = {}
	context_dict['groups'] = Group.objects.all()
	context_dict['streams'] = Stream.objects.all()
	context_dict['posts'] = Post.objects.all()
	return render_to_response("mainstream/index.html", context_dict, context)