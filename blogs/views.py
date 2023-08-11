from django.shortcuts import render
from .models import News

# Create your views here.
def home_page(request):
    all_news = News.objects.all()
    context ={
        'all_news' : all_news
    }
    return render(request, 'blogs/home2.html', context)  

def gene_page(request):
    return render (request, 'blogs/generic.html') 

def travel(request):
    return render (request, 'blogs/travel.html')

def ment(request):
    return render (request, 'blogs/elements.html') 
