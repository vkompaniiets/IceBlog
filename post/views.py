from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404

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
                is_published=form.cleaned_data['is_published'],
                created_by=request.user
            ).save()
            return HttpResponseRedirect(reverse('all_users'))
        else:
            return TemplateResponse(request, 'edit_post.html', {'errors': form.errors})
    else:
        return TemplateResponse(request, 'edit_post.html')


@login_required
def update_by_id(request, post_id):
    if request.method == 'POST':
        form = UpdatePostForm(instance=Post.objects.get(id=post_id), data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('all_users'))
        return TemplateResponse(request, 'edit_post.html', {'errors': form.errors})
    else:
        post = get_object_or_404(Post, id=post_id)

        form = UpdatePostForm(instance=post)
        return TemplateResponse(request, 'edit_post.html',
                                {'form': form, 'edit': True, 'post_id': post_id, 'created_by': post.created_by})


@login_required
def show_by_id(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    return TemplateResponse(request, 'show_post.html', {'post': post})
