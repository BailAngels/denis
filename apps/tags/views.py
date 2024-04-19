from django.shortcuts import render

from apps.tags.models import Tag


def all_posts(request):
    pass


def tag_index(request):
    tags = Tag.objects.all()
    return render(request, 'tag_page.html', locals())