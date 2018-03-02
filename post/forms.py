from django.forms import ModelForm, CharField, BooleanField, Form

from post.models import Post


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'is_published']


class UpdatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'is_published']  # поля которые будем редактировать
