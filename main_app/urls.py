from django.urls import path, include
from main_app.controller import home, category, brand

urlpatterns = [
    path('home/', home.index),

    path('category/create/', category.create, name='categoryCreate'),
    path('category/', category.list),
    path('category/<id>/', category.single),
    path('category/edit/<id>/', category.edit),
    path('category/delete/<id>/', category.delete),

    path('brand/create/', brand.create, name='brandCreate'),
    path('brand/', brand.list),
    path('brand/<id>/', brand.single),
    path('brand/edit/<id>/', brand.edit),
    path('brand/delete/<id>/', brand.delete),
]
