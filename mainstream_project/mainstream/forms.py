from django import forms
from mainstream.models import Group, Stream, Post

class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ('name',)

class StreamForm(forms.ModelForm):
	class Meta:
		model = Stream
		fields = ('topic',)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('content',)

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)