from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, BooleanField, Form

from post.models import Post


class AddPostForm(Form):
    name = CharField(required=True)
    description = CharField(required=False)
    published = BooleanField()


class UpdatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'published']  # поля которые будем редактировать
