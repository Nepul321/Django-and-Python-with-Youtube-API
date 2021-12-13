from django.shortcuts import render
import requests
from src.settings import YOUTUBE_API_KEY

def HomeView(request):
    template = "index.html"
    if request.method == "POST":
       searched = request.POST['searched']
       url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&key={YOUTUBE_API_KEY}&type=video&q={searched}'
       response = requests.get(url)
       data = response.json()['items']
       template = "results.html"
       baseURL = 'https://www.youtube.com/watch?v='
       context = {
          'searched' : searched,
          'data' : data,
          'baseurl' : baseURL
       }
       return render(request, template, context)
    else:
           
        context = {

        }

        return render(request, template, context)