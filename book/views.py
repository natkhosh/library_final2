from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *
from django.core.paginator import Paginator
from django.urls import reverse
from .models import *
from .utils import *
from .forms import BookForm

import json

# Create your views here.


class IndexView(ObjectDetailMixin, View):
    template = 'book/index.html'


class ShopView(ObjectDetailMixin, View):
    template = 'book/shop.html'


class BookSingleView(View):

    def get(self, request):

        return render(request, 'book/book-single.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                      'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                      'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE})


class BookCreate(View):

    def get(self, request):
        form = BookForm()

        return render(request, 'book/book_create.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                         'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                         'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                         'form': form})

    def post(self, request):
        if request.method == 'POST':
            bound_form = BookForm(request.POST, request.FILES)
            if bound_form.is_valid():
                bound_form.save()
                func_st = 'Book created successfully!'
                return render(request, 'book/create_done.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                                 'daily_offer': DAILY_OFFER, 'title': TITLE,
                                                                 'about': ABOUT,
                                                                 'contacts': CONTACTS, 'address': ADDRESS,
                                                                 'website': WEBSITE,
                                                                 'func_st': func_st})
            else:
                return render(request, 'book/book_create.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                             'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                             'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                             'form': bound_form})


class CreateDone(View):

    def get(self, request):

        func_st = 'Book created successfully!'
        return render(request, 'book/create_done.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                         'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                         'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                         'func_st': func_st})


class BookUpdate(View):

    def get(self, request, name):
        book = Book.objects.all().filter(id=name)
        # b = book.get(id=name)
        bound_form = BookForm(book)
        return render(request, 'book/book_update.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                             'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                             'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                             'form': bound_form, 'book': book})
