from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
	class Meta:
		model = CommentModel
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(
				attrs={'class':"form-control mb-4" , 'placeholder':"Enter your name"}),
			'comment': forms.Textarea(
				attrs={'class':"mb-4 form-control", 'placeholder':"Enter your comment"})
		}

