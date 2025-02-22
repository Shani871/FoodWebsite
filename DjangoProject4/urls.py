from django.contrib import admin
from django.urls import path, include

from Website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete_consume, name='delete')
]