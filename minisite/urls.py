from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')), #todo list
    path('minichat/', include('minichat.urls')), #chat
    path('posts/', include('posts.urls')), #posts
    path('', include('core.urls')),

]
