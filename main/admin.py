from django.contrib import admin
from main.models import Post, Comment, Reaction

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reaction)
