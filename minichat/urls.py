from django.urls import path
from minichat.views import mini, delete_comment, delete_all

urlpatterns = [
    path('mini/', mini, name='mini'),
    path('delete/<int:id>/', delete_comment, name='delete'),
    path('delete_all/',delete_all, name='delete_all'),
]