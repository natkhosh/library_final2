from django.shortcuts import render
from .settings.base import *
from .models import *


class ObjectDetailMixin:
    template = None

    def get(self, request):

        books = Book.objects.all()
        return render(request, self.template, context={'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE,
                                                   'books': books})