from django.contrib import admin
from blog.models import Post


# Register your models here.
admin.site.register(Post)
list_display = ('title', 'created_at', 'views')
