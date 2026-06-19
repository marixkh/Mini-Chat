from django.urls import path
from .views import todo, todo_delete

urlpatterns = [
    path('', todo, name='todo' ),
    path('todo_delete/<int:id>/', todo_delete, name='todo_delete'),
]