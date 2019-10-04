from django.shortcuts import render
from django.utils import timezone
from .models import Article
# Create your views here.


def form_page(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'LandingPage/form_page.html', {'posts': posts})

