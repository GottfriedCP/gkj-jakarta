from django.shortcuts import render

# Create your views here.
def home(request):
    request.session['current_page'] = 'home'
    #TODO
    # query 5-10 artikel terbaru
    return render(request, 'homepage/index.html')

def about(request):
    request.session['current_page'] = 'about'
    return render(request, 'homepage/about.html')
