import requests
from django.http import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def random_quotes(request):
   url = 'https://game-of-thrones-quotes.herokuapp.com/v1/random/5' 
   response = requests.get(url)
   data = response.json()
   print(data)
   context = {
       'data': data,
   }
   return render(request, 'apiapp/index.html',context)

    
   