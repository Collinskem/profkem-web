
from django.urls import path, re_path
from . import views
app_name = 'shop'

urlpatterns = [
    path('home', views.product_list, name='product_list'),
    re_path('(?P<category_slug>[-\w]+)/', views.product_list, name='product_list_by_category'),
    re_path('(?P<id>\d+)/(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),


]
