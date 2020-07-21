from digg_paginator import DiggPaginator
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView

from .models import Post, Tag


class Home(ListView):
    model = Post
    paginate_by = 3
    template_name = 'blog.html'
    paginator_class = DiggPaginator

    def get_queryset(self, *args, **kwargs):
        qs = super(Home, self).get_queryset(*args, **kwargs).exclude(draft=True)

        # Este try sirve para que no se repita mas de 1 vez los resultados?
        try:
            qs = qs.filter(slug__exact=self.kwargs['slug'])
        except:
            pass

        if 'q' in self.request.GET:
            query = self.request.GET['q']
            qs = (qs.filter(title__icontains=query)).distinct()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        if 'q' in self.request.GET:
            context['q'] = self.request.GET['q']
            context['title'] = 'Resultados de la busqueda'

        try:
            context['slug'] = self.kwargs['slug']
        except:
            context['slug'] = None

        if not context['slug'] is None:
            slug = get_object_or_404(Tag.objects.filter(slug__exact=self.kwargs['slug']))
            context['tags'] = Post.objects.filter(tags=slug)
        return context


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', locals())


def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        form = AuthenticationForm()
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    do_login(request, user)
                    return redirect('/dashboard')
            else:
                message = 'El usuario no existe o los datos son incorrectos'
    return render(request, 'login.html', locals())


def logout(request):
    if request.user.is_authenticated is False:
        return redirect('/login')
    do_logout(request)
    return redirect('/')
