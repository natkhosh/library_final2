from django.shortcuts import render
from websocket import create_connection

from .settings.base import *
from django.http import HttpResponse
from .models import *


import json


class ObjectDetailMixin:
    template = None

    def get(self, request):

        # bc = "WS_test"
        # ws = create_connection('ws://localhost:8000/')
        # ws.send("books?")
        # bc = str(ws.recv().format())

        books_query = Book.objects.all().values()
        books = list(books_query)

        if not request.is_ajax():
            return render(request, self.template, context={'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                           'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                           'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                           'book_count': '0', 'books': books})
        else:

            return HttpResponse(json.dumps({'books': books}), content_type='application/json')


