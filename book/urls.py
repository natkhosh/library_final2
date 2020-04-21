from django.urls import path
from .views import *




urlpatterns = [
    path('', IndexView.as_view(),  name='home'),
    path('book/', BookView.as_view(), name='book'),
    # path('book/<int:page_id>', BookView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('book_single/', BookSingleView.as_view(), name='book_single'),

]

