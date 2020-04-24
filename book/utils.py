from django.shortcuts import render
from .settings.base import *
from django.http import HttpResponse
from .models import *

import json


class ObjectDetailMixin:
    template = None

    def get(self, request):

        # books = Book.objects.all()

        books_query = Book.objects.all().values()
        books = list(books_query)

        if not request.is_ajax():
            return render(request, self.template, context={'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                           'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                           'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                           'books': books})
        else:
            return HttpResponse(json.dumps({'books': books}), content_type='application/json')


