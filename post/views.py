from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from post.models import Post
from post.forms import AddPostForm, UpdatePostForm


@login_required
def create(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)

        if form.is_valid():
            Post(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                published=form.cleaned_data['published'],
                created_by=request.user
            ).save()
            return HttpResponseRedirect(reverse('all_users'))
        else:
            return TemplateResponse(request, 'edit_post.html', {'errors': form.errors})
    else:
        users = list(User.objects.all())
        return TemplateResponse(request, 'edit_post.html', {'users': users})


@login_required
def update_by_id(request, post_id):
    if request.method == 'POST':
        form = UpdatePostForm(instance=Post.objects.get(id=post_id), data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('all_users'))
        return TemplateResponse(request, 'edit_post.html', {'errors': form.errors})
    else:
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise Http404

        form = UpdatePostForm(instance=post)
        return TemplateResponse(request, 'edit_post.html',
                                {'form': form, 'edit': True, 'post_id': post_id, 'created_by': post.created_by})


@login_required
def show_by_id(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404  # если пост не найден - выдать ошибку 404
    return TemplateResponse(request, 'show_post.html', {'post': post})
