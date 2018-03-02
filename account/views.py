from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.urls import reverse

from post.models import Post


def account_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return HttpResponseRedirect(reverse('all_users'))
        else:
            return TemplateResponse(request, 'login.html', {'error': True})
    else:
        return TemplateResponse(request, 'login.html', {})


@login_required
def account_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def show_all_users(request):
    data = User.objects.all()

    return TemplateResponse(request, 'all_users.html', {
        'users': data
    })


@login_required
def detail(request, user_id):
    posts = Post.objects.filter(created_by=user_id, is_published=True)

    return TemplateResponse(request, 'user_posts.html', {
        'posts': posts
    })
