from django.urls import path

from apps.blogs.views import (
    homepage,
    create,
    retrieve,
    destroy,
    update
    )


urlpatterns = [
    path('', homepage, name='index'),
    path('create/',create,name='create'),
    path('detail/<int:pk>/',retrieve,name='detail'),
    path('delete/<int:pk>/',destroy,name='delete'),
    path('update/<int:pk>/', update,name='update'),
]
