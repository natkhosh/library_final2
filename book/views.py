from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *
from django.core.paginator import Paginator
from django.urls import reverse
from .models import *


# Create your views here.

class IndexView(View):

    def get(self, request):

        return render(request, 'book/index.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE})


class ShopView(View):

    def get(self, request):

        books_list = [{'author': 'J. K. Rowling',
                       'name': "Harry Potter and the Philosopher's Stone",
                       'image': '/book/images/product_1.jpg',
                       'year_publication': '1997',
                       'price': '$25.00',
                       'discount': '10%',
                       'price_sale': '$22.50'},
                      {'author': 'J. K. Rowling',
                       'name': "Harry Potter and the Chamber of Secrets",
                       'image': '/book/images/product_2.jpg',
                       'year_publication': '1998',
                       'price': '$25.00',
                       'discount': '10%',
                       'price_sale': '$22.50'},
                      {'author': 'J. K. Rowling',
                       'name': "Harry Potter and the Chamber of Secrets",
                       'image': '/book/images/product_2.jpg',
                       'year_publication': '1998',
                       'price': '$25.00',
                       'discount': '10%',
                       'price_sale': '$22.50'},


                      ]

        return render(request, 'book/shop.html',  {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE})

class BookSingleView(View):

    def get(self, request):

        return render(request, 'book/book-single.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                      'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                      'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE})


class BookView(View):

    def get(self, request, page_id=1):




        products_list = Product.objects.all()

        paginator = Paginator(products_list, 4)

        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('book'))
        return render(request, 'book/shop.html',  {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS, 'products': products})


