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
from websocket import create_connection

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
                                                      'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                        'book_count': BOOK_COUNT})


class BookCreate(View):
    func = 'Book created'
    def get(self, request):
        form = BookForm()

        return render(request, 'book/book_create.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                         'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                         'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                         'book_count': BOOK_COUNT, 'form': form})

    def post(self, request):
        if request.method == 'POST':
            bound_form = BookForm(request.POST, request.FILES)
            if bound_form.is_valid():
                bound_form.save()
                func_st = 'Book created successfully!'

                return render(request, 'book/done.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                                 'daily_offer': DAILY_OFFER, 'title': TITLE,
                                                                 'about': ABOUT,
                                                                 'contacts': CONTACTS, 'address': ADDRESS,
                                                                 'website': WEBSITE,  'book_count': BOOK_COUNT,
                                                                 'func_st': func_st})
            else:
                return render(request, 'book/book_create.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                             'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                             'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                                 'book_count': BOOK_COUNT,
                                                             'form': bound_form})


class BookUpdate(View):

    def get(self, request):
        book = Book.objects.all()


        return render(request, 'book/book_update.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                       'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                       'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                         'book_count': BOOK_COUNT,
                                                       'book': book})


# class BookUp(View):
#
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         bound_form = BookForm(istance=book)
#         return render(request, 'book/book_update.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
#                                                        'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
#                                                        'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
#                                                        'book': book})




def edit(request, id):      # изменение данных в бд
    try:
        book = Book.objects.get(id=id)
        bound_form = BookForm(instance=book)

        if request.method == "POST":
            bound_form.save()
            return render(request, 'book/done.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                      'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                      'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                      'book_count': BOOK_COUNT,
                                                      'book': book, 'form': bound_form})
        else:
            return render(request, 'book/book_edit.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                      'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                      'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                           'book_count': BOOK_COUNT,
                                                      'book': book, 'form': bound_form})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Sorry, Book not found</h2>")



def delete(request, id):    # удаление данных из бд
    try:
        book = Book.objects.get(id=id)
        book.delete()
        func_st = 'Book deleted successfully!'
        return render(request, 'book/done.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                  'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                  'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                  'book_count': BOOK_COUNT,
                                                  'func_st': func_st})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Sorry, Book not found</h2>")


def create_done(request):

    func_st = 'Book created successfully!'
    return render(request, 'book/done.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                     'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                     'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                    'book_count': BOOK_COUNT, 'func_st': func_st})


def edit_done(request):

    func_st = 'Book edited successfully!'
    return render(request, 'book/done.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                     'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                     'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                    'book_count': BOOK_COUNT, 'func_st': func_st})


def delete_done(request):

    func_st = 'Book deleted successfully!'
    return render(request, 'book/done.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                     'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                     'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                    'book_count': BOOK_COUNT,'func_st': func_st})
