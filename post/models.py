from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CharField, BooleanField, DateTimeField, TextField, DO_NOTHING


class Post(Model):
    created_by = ForeignKey(User, blank=True, null=True, on_delete=DO_NOTHING)
    name = CharField(max_length=50)
    published = BooleanField(default=False)
    description = TextField(blank=True, null=True, default=None)
    created = DateTimeField(auto_now_add=True, auto_now=False)
    updated = DateTimeField(auto_now_add=False, auto_now=True)
