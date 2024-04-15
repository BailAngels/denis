from django.shortcuts import render,redirect

from apps.blogs.models import Blog


def homepage(request):
    blogs = Blog.objects.all()
    return render(request, 'homepage.html', locals())


def create(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        text = request.POST.get('description')
        photo = request.FILES.get('image')
        blog = Blog.objects.create(title=name,description=text,image=photo)
        return redirect('index')
    return render(request,'create.html')


def retrieve(request,pk):
    blogs = Blog.objects.get(id=pk)
    return render(request,'detail.html',locals())


def update(request,pk):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        blog = Blog.objects.get(id=pk)
        blog.title = title
        blog.description = description
        blog.image = image
        blog.save()
        return redirect('detail', blog.id)
    return render(request,'update.html')


def destroy(request,pk):
    if request.method == 'POST':
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('index')
    return render(request,'delete.html')