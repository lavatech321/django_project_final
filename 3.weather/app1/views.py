from django.shortcuts import render, redirect
import requests
from .models import CityModel
from .forms import CityForm

def home(request):
	
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=029db852173d8ee15ccb004dffc4586c'
	#city = 'Mumbai'
	# code = requests.get(url.format(city))
	# print(code.text)
	# code = requests.get(url.format(city)).json()
	# print(code)
	
	#code = requests.get(url.format(city)).json()

	#city_weather = {
	#	'city' : city,
	#	'temperature' : code['main']['temp'],
	#	'description': code['weather'][0]['description'],
	#	'icon': code['weather'][0]['icon'],
	#}

	#print(city_weather)
	# context = { 'all_weather' : city_weather } 
	# return render( request, 'app1/3-weather.html', context)
	err_msg = ''
	err_status = ''

	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			new_city = form.cleaned_data['name']
			final_city = CityModel.objects.filter(name=new_city).count()
			if final_city == 0:
				mycode = requests.get(url.format(new_city)).json()		
				if mycode['cod'] == 200:
					form.save()
					return redirect('home')
				else:
					err_msg = 'Invalid City name'
					err_status = 'alert-danger'	
			else:
				err_msg = 'City Already Exists'
				err_status = 'alert-danger'
	else:
		form = CityForm()
	cities = CityModel.objects.all()
	all_weather = []

	for x in cities:
		code = requests.get(url.format(x.name)).json()
		city_weather = {
			'city' : x.name,
			'temperature' : code['main']['temp'],
			'description': code['weather'][0]['description'],
			'icon': code['weather'][0]['icon'],
		}
		all_weather.append(city_weather)
	context = { 
		'all_weather' : all_weather , 
		'form': form ,
		'message': err_msg ,
		'message_status': err_status,
		} 
	return render( request, 'app1/3-weather.html', context)
# Create your views here.
