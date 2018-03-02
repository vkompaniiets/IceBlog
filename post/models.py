from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CharField, BooleanField, DateTimeField, TextField, CASCADE
from tinymce.models import HTMLField


class Post(Model):
    created_by = ForeignKey(User, blank=True, null=True, on_delete=CASCADE)
    name = CharField(max_length=50)
    is_published = BooleanField(default=False)
    description = HTMLField()
    created_at = DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = DateTimeField(auto_now_add=False, auto_now=True)
