from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *
from django.core.paginator import Paginator
from django.urls import reverse
from .models import *
from .utils import *
from .forms import BookForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

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

    def get(self, request):
        book = Book.objects.all()

        return render(request, 'book/book_update.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                       'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                       'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                       'book': book})


def edit(request, id):      # изменение данных в бд
    try:
        book = Book.objects.get(id=id)
        print('$$$$$$$$$$$$$$$$', book)

        if request.method == "POST":
            book.author = request.POST.get("author")
            book.name = request.POST.get("name")
            book.image = request.POST.get("image")
            book.year_publication = request.POST.get("year_publication")
            book.price = request.POST.get("price")
            book.discount = request.POST.get("discount")
            book.price_sale = request.POST.get("price_sale")
            book.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'book/book_edit.html', {'book': book})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Sorry, Book not found</h2>")


def delete(request, id):    # удаление данных из бд
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/")
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Sorry, Book not found</h2>")