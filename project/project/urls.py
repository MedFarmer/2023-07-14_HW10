
from django.contrib import admin
from django.urls import path
from app.views import index, adding_id, add_student, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('adding_id/', adding_id, name='adding_id'),
    path('add_student/', add_student, name='add_student'),
    path('delete/', delete, name='delete'),
]
