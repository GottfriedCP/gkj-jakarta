from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ArticleForm
from .models import Article

def index(request):
    request.session['current_page'] = 'blog'
    art_list = Article.objects.filter(published=True)
    paginator = Paginator(art_list, 15, orphans=3)

    page = request.GET.get('page')
    arts = paginator.get_page(page)

    return render(request, 'blog/index.html', {
        'arts': arts,
    })

def article(request, year, slug):
    request.session['current_page'] = 'blog'
    art = get_object_or_404(Article, date_created__year=year, slug=slug, published=True)
    return render(request, 'blog/article.html', {
        'art': art,
        'debug': settings.DEBUG,
    })

@login_required
def create(request):
    request.session['current_page'] = 'blog'
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            art = form.save()
            if art.published:
                return redirect(art)
            else:
                return redirect('blog:index')
    return render(request, 'blog/create.html', {
        'form': form,
    })

@login_required
def edit(request, year, slug):
    request.session['current_page'] = 'blog'
    art = get_object_or_404(Article, date_created__year=year, slug=slug)
    art_year = art.date_created.year
    art_slug = art.slug
    form = ArticleForm(instance=art)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=art)
        if form.is_valid():
            art = form.save()
            if art.published:
                return redirect(art)
            else:
                return redirect('blog:index')
    return render(request, 'blog/edit.html', {
        'art_year': art_year,
        'art_slug': art_slug,
        'form': form,
    })

@login_required
def list_all(request):
    """List all articles in table."""
    art_list = Article.objects.all()
    paginator = Paginator(art_list, 50, orphans=3)

    page = request.GET.get('page')
    arts = paginator.get_page(page)

    return render(request, 'blog/list.html', {
        'arts': arts,
    })
