from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hope/', views.hope_list, name='hope list'),
    path('details/<int:id>', views.hope_detail, name='hope detail'),

]