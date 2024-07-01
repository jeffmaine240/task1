from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET

import requests
# Create your views here.

ip_address_url = 'https://get.geojs.io/v1/ip.json'
ip_to_city_url = "https://ipinfo.io/{}/geo"
weather_key = "f8505e1d5282111e5bd07d586c595083"
weather_url = 'https://api.openweathermap.org/data/2.5/weather'

class HelloView(View):
    @method_decorator(require_GET)
    def get(self, request):
        name = request.GET.get('visitor_name')
        data = requests.get(url=ip_address_url)
        response = data.json()
        client_ip = response['ip']
        data1 = requests.get(ip_to_city_url.format(client_ip))
        response1 = data1.json()
        print(response1)
        city = response1['city']
        parameter = {
            'q':city,
            'appid': weather_key
        }
        data2 = requests.get(url=weather_url, params=parameter)
        response2 = data2.json()
        temp_in_f = response2['main']['temp']
        temp = temp_in_f - 273.15
        greeting = f"Hello, {name}!, the temperature is {temp:.2f} degrees celcius in {city}"
        return JsonResponse({
            'client_ip': client_ip, 
            'location': city,
            'greeting': greeting,
        })
     
      