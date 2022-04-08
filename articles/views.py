from ast import Delete
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from articles.forms import ArticleCreatedForm
from .models import Articles
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def home_view(request):
    object_list = Articles.objects.all()
    context = {
        'object_list':object_list
    }
    return render(request, 'articles/index.html', context)
@login_required
def my_articles_view(request):
    object_list = Articles.objects.filter(author=request.user)
    context = {
        'object_list':object_list
    }
    return render(request, 'articles/index.html', context)

@login_required
def detail_view(request, slug):#, year, month, day
    obj = Articles.objects.get(slug=slug)
    context = {
        'object' : obj
    }
    return render(request, 'articles/detail.html', context)
@login_required
def search_article(request):
    obj = None
    if request.method == "POST":
        query = request.POST.get('qy')
      
        #obj = Articles.objects.filter(Q(title__icontains = query)| Q(content__icontains = query))
        # lookups = Q(title__icontains = query)| Q(content__icontains = query)
        # obj = Articles.objects.filter(lookups)
        obj = Articles.objects.search(query)
        if not obj:
                messages.error(request, 'siz qidirgan article chiqmadi !!')
                return redirect('/articles/search')
    context = {
            'object':obj
        }
    return render(request, 'articles/search.html', context)
@login_required
def create_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content :
            obj = Articles.objects.create(title = title, content = content)
        else:
            messages.error(request, 'siz qidirgan article chiqmadi !!')
            redirect('/articles/search')
    return render(request, 'articles/create.html', {})

def _form_created(request):
    form = ArticleCreatedForm()
    obj = None
    if request.method == 'POST':
        form = ArticleCreatedForm(request.POST)
        if form.is_valid():
            obj = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # obj = Articles.objects.create(title = title, content = content)
    context = {
        'form': form,
        'obj' : obj
    }
    return render(request, 'articles/create.html', context)
@login_required
def form_created(request):
    form = ArticleCreatedForm()
    obj = None
    if request.method == 'POST':
        form = ArticleCreatedForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form.save_m2m()
    context = {
        'form' : form,
        'obj' : obj
    }
    return render(request, 'articles/create.html', context)
    form = ArticleCreatedForm(request.POST or None)
    obj = None 
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form.save_m2m()
    context = {
        'form' : form,
        'obj' : obj
    }
    return render(request, 'articles/create.html', context)

@login_required
def article_update(request, slug):
    obj = get_object_or_404(Articles, slug=slug)
    form = ArticleCreatedForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('detail_index', kwargs = {'slug':slug}))
    context = {
        'form':form,
        'obj':obj
    }
    return render(request, 'articles/update.html', context)

def article_delate(request, slug):
    obj = get_object_or_404(Articles, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect('/articles/')
    return render(request, 'articles/delete.html')

