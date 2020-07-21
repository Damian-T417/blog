import json

from digg_paginator import DiggPaginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.http import JsonResponse, HttpResponse

from blog.models import Post, Tag

from .forms import PostForm, TagForm

# Create your views here.


@method_decorator(login_required, name='dispatch')
class Posts(ListView):
    model = Post
    paginate_by = 5
    template_name = 'postsView.html'
    paginator_class = DiggPaginator

    def get_queryset(self, *args, **kwargs):
        qs = super(Posts, self).get_queryset(*args, **kwargs)
        if 'q' in self.request.GET:
            query = self.request.GET['q']
            qs = (qs.filter(title__icontains=query)).distinct()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(Posts, self).get_context_data(*args, **kwargs)
        if 'q' in self.request.GET:
            context['q'] = self.request.GET['q']
            context['title'] = 'Resultados de la busqueda'
        return context

    # Forbideen 403  
    def delete_post(request, id):
        if request.user.is_authenticated is False:
            return redirect('/login')
        object = get_object_or_404(Post, id=id)
        if request.method == 'POST':
            object.delete()
        
        return JsonResponse(
            {
                'content': {
                    'message': 'El post se ha borrado con exito',
                }
            }
        )


@method_decorator(login_required, name='dispatch')
class Tags(ListView):
    model = Tag
    paginate_by = 5
    template_name = 'tagsView.html'
    paginator_class = DiggPaginator

    def get_queryset(self, *args, **kwargs):
        qs = super(Tags, self).get_queryset(*args, **kwargs)
        if 'q' in self.request.GET:
            query = self.request.GET['q']
            qs = (qs.filter(name__icontains=query)).distinct()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(Tags, self).get_context_data(*args, **kwargs)
        if 'q' in self.request.GET:
            context['q'] = self.request.GET['q']
            context['title'] = 'Resultados de la busqueda'
        return context


def dashboard(request):
    if request.user.is_authenticated:
        total_post = Post.objects.all().count()
        total_tag = Tag.objects.all().count()
        return render(request, 'dashboardView.html', locals())
    return redirect('/login')

def get_action(request):
    object_list = Post.objects.all()
    ajax_response = True
    to_json = {
        'ajax_response': ajax_response
    }
    user_list = []
    for post in object_list:
        result = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
        }
        user_list.append(result)
    # print(user_list)
    json_dump = json.dumps(
        {
            'to_json': True,
            'user_list': user_list
        },
        indent=3
    )
    print(json_dump)
    return HttpResponse(
        json_dump,
        content_type='application/json'
    )


def new_post(request):
    if request.user.is_authenticated is False:
        return redirect('/login')
    title = 'Agregar una publicación'
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            save_form = form.save()
            save_form.save()
            message = 'La publicación ha sido publicada correctamente'
    form = PostForm()
    return render(request, 'dashboardForm.html', locals())


def edit_post(request, id):
    if request.user.is_authenticated is False:
        return redirect('/login')
    title = 'Editar una publicación'
    object = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            save_form = form.save()
            message = 'La publicación ha sido modificada correctamente'
    form = PostForm(instance=object)
    return render(request, 'dashboardForm.html', locals())

"""
def delete_post(request, id):
    if request.user.is_authenticated is False:
        return redirect('/login')
    object = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        object.delete()
        message = 'La publicación se ha borrado con exito'
    form = PostForm()
    return render(request, 'dashboardForm.html', locals())
"""


def new_tag(request):
    if request.user.is_authenticated is False:
        return redirect('/login')
    title = 'Agregar una etiqueta'
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            save_form = form.save()
            save_form.save()
            message = 'La etiqueta ha sido creada correctamente'
    form = TagForm()
    return render(request, 'dashboardForm.html', locals())


def edit_tag(request, id):
    if request.user.is_authenticated is False:
        return redirect('/login')
    title = 'Editar una etiqueta'
    object = get_object_or_404(Tag, id=id)
    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            save_form = form.save()
            message = 'La etiqueta ha sido modificado correctamente'
    form = TagForm(instance=object)
    return render(request, 'dashboardForm.html', locals())


def delete_tag(request, id):
    if request.user.is_authenticated is False:
        return redirect('/login')
    object = get_object_or_404(Tag, id=id)
    if request.method == 'POST':
        object.delete()
        message = 'La etiqueta se ha eliminado correctamente'
    form = TagForm()
    return render(request, 'dashboardForm.html', locals())
