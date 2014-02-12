from django import forms
from mainstream.models import Group

class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ('name',)