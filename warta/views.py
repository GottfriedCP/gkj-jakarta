from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import WartaForm
from .models import Warta
import datetime, time, os, hashlib, uuid

def index(request):
    request.session['current_page'] = None
    
    wartas = Warta.objects.all()
    latest_warta_url = False
    try:
        latest_warta_url = 'http://' + request.get_host() + wartas[0].warta.url
    except:
        print('Cannot get warta url.')

    return render(request, 'warta/index.html', {
        'wartas': wartas,
        'latest_warta_url': latest_warta_url,
    })

@login_required
def create(request):
    """Example of WG:\n
    Filename: wg20181219[hash]/WG-2018-12-19.pdf\n
    Shortname: WG-2018-12-19.pdf    
    """
    request.session['current_page'] = None

    form = WartaForm()
    randuuid = str(uuid.uuid4())
    randhash = hashlib.sha1(randuuid.encode('utf-8')).hexdigest()
    if request.method == 'POST':
        form = WartaForm(request.POST, request.FILES)
        if form.is_valid():
            warta = form.save()
            init_path = warta.warta.path
            warta.warta.name = time.strftime('wg/%Y/%m/%d/WG-%Y-%m-%d-{}.pdf'.format(randhash))
            new_path = settings.MEDIA_ROOT + warta.warta.name
            os.rename(init_path, new_path)
            print('New warta named {}'.format(warta.warta.path))
            warta.save()
            # Delete warta older than 1 year (365 days)
            _delete_old_wartas()
            return redirect('warta:list')
    return render(request, 'warta/create.html', {
        'form': form,
    })

def _delete_old_wartas():
    """Delete wartas older than one year."""
    one_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)
    old_wartas = Warta.objects.filter(date_uploaded__lt=one_year_ago)
    old_wartas.delete()
