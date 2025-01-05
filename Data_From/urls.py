from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('sign',views.sign, name='sign'),
    path('cong',views.cong, name='cong'),
    # path('product_list',views.product_list, name='product_list'),
]
