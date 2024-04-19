from django.urls import path

from apps.tags.views import tag_index


urlpatterns = [
    path('tags/', tag_index,name='tag_index'),
]
