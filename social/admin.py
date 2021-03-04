from django.contrib import admin
from .models import Post, Perfil, Relationship
# Register your models here.
admin.site.register(Perfil)
admin.site.register(Post)
admin.site.register(Relationship)