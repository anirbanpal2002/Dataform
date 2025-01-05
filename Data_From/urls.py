from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home',views.home, name='home'),
    path('product_list',views.product_list, name='product_list'),
]
