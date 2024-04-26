from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib import messages

from apps.blogs.models import Blog, BlogLike
from apps.tags.models import Tag
from apps.comments.models import Comment


def homepage(request):
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        blogs = Blog.objects.filter(Q(title__icontains=key) | Q(author__username__icontains=key))
    else:
        blogs = Blog.objects.all()
    return render(request, 'homepage.html', locals())


def create(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        text = request.POST.get('description')
        photo = request.FILES.get('image')
        tags_input = request.POST.get('tags')
        
        blog_create = Blog.objects.create(author=request.user, title=name, description=text, image=photo)
        
        if tags_input:
            tags_list = [tag.strip() for tag in tags_input.split(',')]
            for tag_title in tags_list:
                tag_obj, created = Tag.objects.get_or_create(title=tag_title)
                tag_obj.blog.add(blog_create)
        
        return redirect('index')
    
    return render(request, 'blogs/create.html')



def retrieve(request,pk):
    blogs = Blog.objects.get(id=pk)
    if request.method=='POST':
        if 'like' in request.POST:
            try:
                like = BlogLike.objects.get(user = request.user, blog = blogs)
                like.delete()
            except:
                BlogLike.objects.create(user = request.user, blog = blogs)
        if 'comment' in request.POST:
            try:
                text = request.POST['text']
                comment_create = Comment.objects.create(user = request.user, blog = blogs, text = text)
                return redirect('detail', blogs.id)
            except:            
                messages.error(request, 'ошибка у вас')
    
    return render(request,'blogs/detail.html',locals())



def update(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        tags_input = request.POST['tags_input']

        # Обновляем основные данные блога
        blog.title = title
        blog.description = description
        blog.image = image
        blog.save()

        # Обновляем теги блога
        if tags_input:
            tags_list = [tag.strip() for tag in tags_input.split(',')]
            updated_tags = []

            # Обновляем существующие теги и создаем новые
            for tag_title in tags_list:
                tag_obj, created = Tag.objects.get_or_create(title=tag_title)
                tag_obj.blog.add(blog)
                updated_tags.append(tag_obj)

            # Удаляем теги, которые были удалены
            blog.tags.exclude(id__in=[tag.id for tag in updated_tags]).delete()

        return redirect('detail', blog.id)

    # Передаем данные блога и его тегов в шаблон
    tags = blog.tags.all()
    tag_titles = ', '.join([tag.title for tag in tags])
    return render(request, 'blogs/update.html', {'blog': blog, 'tags': tags, 'tag_titles': tag_titles})



def destroy(request,pk):
    if request.method == 'POST':
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('index')
    return render(request,'blogs/delete.html')


