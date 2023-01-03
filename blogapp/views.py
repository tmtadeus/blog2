from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404

from blogapp.models import ArticleModel

from .forms import ArticleForm, LoginForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', context={'form': form})
    if request.POST['password1'] != request.POST['password2']:
        form = UserCreationForm(request.POST)
        return render(request, 'signup.html', context={
            'form': form, 'error': 'Passwords do not match'
            })
    form = UserCreationForm(request.POST)
    user = User.objects.create_user(username=request.POST['username'],
                                    password=request.POST['password1'])
    user.save()
    login(request=request, user=user)

    return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})
    user = authenticate(request,
                        username=request.POST['username'],
                        password=request.POST['password'])
    if not user:
        form = LoginForm(request.POST)
        return render(request, 'login.html', context={'form':form,
                                                      'error': 'User not found'})
    login(request, user=user)
    return redirect('home')



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return redirect('home')

def articles(request):

    articles = ArticleModel.objects.filter(author=request.user)[:2]
    return render(request, 'articles.html', context={'articles': articles})


def detail(request, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id, author=request.user)
    return render(request, 'detail.html', context={'article': article})


def create_article(request):
    if request.method == 'GET':
        article_form = ArticleForm()
        return render(request, 'create_article.html', {'form': article_form})
    article_form = ArticleForm(request.POST)
    new_article = article_form.save(commit=False)
    new_article.author = request.user
    new_article.save()
    return redirect('home')
