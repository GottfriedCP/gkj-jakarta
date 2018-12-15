from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from blog.models import Article

# Create your views here.
def home(request):
    request.session['current_page'] = 'home'
    arts5 = Article.objects.filter(published=True)[:5]
    return render(request, 'homepage/index.html', {
        'arts': arts5,
    })

def about(request):
    request.session['current_page'] = 'about'
    return render(request, 'homepage/about.html')

def login_view(request):
    request.session['current_page'] = None
    if request.user.is_authenticated:
        return redirect('homepage:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next-page')
        u = authenticate(request, username=username, password=password)
        if u is not None:
            login(request, u)
            if next_page:
                return redirect(next_page)
            else:
                return redirect('homepage:home')
        else:
            messages.error(request, 'Username or password incorrect.')
    return render(request, 'homepage/login.html', {
        'next_page': request.GET.get('next'),
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage:home')
