from django.contrib import admin
from django.urls import path, include
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('submit/', views.submit_form, name='submit_form'),

]
