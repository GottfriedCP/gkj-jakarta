from decouple import config, Csv
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from blog.models import Article
import random, requests

# Create your views here.
def home(request):
    request.session['current_page'] = 'home'
    # Five latest blog articles
    arts5 = Article.objects.filter(published=True)[:5]
    # Our daily bread
    uri = 'http://alkitab.sabda.org/api/vod.php?format=jsonp'
    try:
        bread = requests.get(uri).json()['html']
    except:
        bread = False
        print('Cannot get our daily bread.')
    return render(request, 'homepage/index.html', {
        'arts': arts5,
        'bread': bread,
    })

def gallery(request):
    request.session['current_page'] = 'gallery'
    return render(request, 'homepage/gallery.html')

def about(request):
    request.session['current_page'] = 'about'
    return render(request, 'homepage/about.html')

def contact_us(request):
    request.session['current_page'] = 'contact-us'
    if request.method == 'POST':
        # Verify security question first
        sender_answer = int(request.POST.get('sender-answer', -1))
        if sender_answer != request.session['security_answer']:
            print('Security challenge response invalid.')
            return redirect('homepage:contact_us')

        sender_name = request.POST.get('name')
        sender_email = request.POST.get('email')
        message = request.POST.get('message')
        message = 'Pesan ini dikirim oleh {} ({}).\n\n\n{}'.format(sender_name, sender_email, message)
        
        # Compose email
        email = EmailMessage(
            '[Website GKJJ] Pesan dari {}'.format(sender_name),
            message,
            config('EMAIL_HOST_USER'),
            config('RECIPIENT', cast=Csv()),
            reply_to=[sender_email, ],
        )
        # Attempt to send email
        try:
            email.send()
        except:
            import sys
            print('Email not sent: {}'.format(sys.exc_info()[1]))

        request.session['message_sent'] = True
    
    operand1 = random.randint(1, 50)
    operand2 = random.randint(1, 50)
    security_question = '{} + {} = '.format(operand1, operand2)
    request.session['security_answer'] = operand1 + operand2
    
    message_sent = request.session.get('message_sent', False)
    try:
        del request.session['message_sent']
    except KeyError:
        pass
    return render(request, 'homepage/contact-us.html', {
        'message_sent': message_sent,
        'security_question': security_question,
    })

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
