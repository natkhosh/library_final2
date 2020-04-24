from django.urls import path
from .views import *
from . import views




urlpatterns = [
    path('', IndexView.as_view(),  name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('book_single/', BookSingleView.as_view(), name='book_single'),
    path('create/', BookCreate.as_view(), name='book_create'),
    path('update/edit/<int:id>/', views.edit, name='book_edit'),
    path("create_done/", views.create_done,  name='create_done'),
    path("edit_done/", views.edit_done,  name='edit_done'),
    path("update/", BookUpdate.as_view(),  name='book_update'),
    path('delete/<int:id>/', views.delete, name='book_delete')
]

