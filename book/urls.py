from django.urls import path
from .views import *




urlpatterns = [
    path('', IndexView.as_view(),  name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('book_single/', BookSingleView.as_view(), name='book_single'),
    path('create/', BookCreate.as_view(), name='book_create')
    # path('book/', BookView.as_view(), name='book'),
    # path('book/<int:page_id>', BookView.as_view()),
]

