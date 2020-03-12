from django import forms 
from .models import TodoModel

class TodoForm(forms.ModelForm):
	class Meta:
		fields = '__all__'
		model = TodoModel
		widgets = {
			'text': forms.TextInput(
				attrs = { 'class':"lightline form-control" , 'placeholder': 'Enter your todo' }),
		}