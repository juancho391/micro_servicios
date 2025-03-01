"""
URL configuration for products_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import ListProducts,ProductDetail,FilterProductsByPrice, GetProductsByName, GetProductsByCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docs.urls')),
    path('products/', ListProducts.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('filterproducts/<int:price>', FilterProductsByPrice.as_view()),
    path('filterproducts/<str:name>', GetProductsByName.as_view()),
    path('categoryfilterproduct/<str:category_name>', GetProductsByCategory.as_view()),

]
