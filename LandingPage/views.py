from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from multiurl import ContinueResolving

from .models import Article
from .forms import UserForm
# Create your views here.



def form_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LandingPage:thank_you')
    else:
        form = UserForm()
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'LandingPage/form_page.html', {'form': form, 'posts': posts})



# Thank you page.
def thank_you(request):
    return render(request, 'LandingPage/thank_you_page.html', {})



















# Add user form
#def form_page(request):

    #if request.method == 'POST':
        #form = UserForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('LandingPage:form_page')
    #else:
        #form = UserForm()
        #return render(request, 'LandingPage/form_page.html', {'form': form})
    #posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'LandingPage/form_page.html', {'posts': posts})





#def form_page(request):
    #posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'LandingPage/form_page.html', {'posts': posts})


# Add user form
#def user(request):
    #if request.method == 'POST':
        #form = UserForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('LandingPage:form_page')
    #else:
        #form = UserForm()
    #return render(request, 'LandingPage/user.html', {'form': form})


