from django import forms
from .models import CityModel

class CityForm(forms.ModelForm):
	class Meta:
		model = CityModel
		fields = '__all__'

		widgets = {
			'name' : forms.TextInput(
				attrs = { 'class':"form-control"  , 'placeholder':"Enter city" })
		}