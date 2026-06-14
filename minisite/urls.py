from django.contrib import admin
from django.urls import path
from core.views import home, delete_comment, delete_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('delete/<int:id>/', delete_comment, name='delete'),
    path('delete_all/',delete_all, name='delete_all'),
]
