from django.shortcuts import render
from .utils import *

# Create your views here.
def home(request):
    # url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-08-20&sortBy=publishedAt&apiKey=a6a9d62ef447454b943368b6af53c929'
    # get_news_from_api(url)
    return render(request, 'home.html', context={'articles':Articles.objects.all()})