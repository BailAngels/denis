from django.contrib import admin

from apps.blogs.models import Blog, BlogLike


admin.site.register(Blog)
admin.site.register(BlogLike)