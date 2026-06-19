from django.urls import path
from .views import posts, delete_post, edit_post


urlpatterns = [
        path('', posts, name='posts'),
        path('delete/<int:id>/', delete_post ,name='delete_post'),
        path('edit/<int:id>/', edit_post, name='edit_post'),
]
