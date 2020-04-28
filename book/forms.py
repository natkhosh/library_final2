from django import forms
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile


class BookForm(forms.Form):
    author = forms.CharField(max_length=50)
    name = forms.CharField(max_length=200)
    image = forms.ImageField()
    year_publication = forms.CharField(max_length=4)
    price = forms.CharField(max_length=10)
    discount = forms.CharField(max_length=10)
    price_sale = forms.CharField(max_length=10)

    author.widget.attrs.update({'class': 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    image.widget.attrs.update({'c lass': 'form-control'})
    year_publication.widget.attrs.update({'class': 'form-control'})
    price.widget.attrs.update({'class': 'form-control'})
    discount.widget.attrs.update({'class': 'form-control'})
    price_sale.widget.attrs.update({'class': 'form-control'})

    # def get(self):
    #     pass

    def save(self):
        new_b = Book.objects.create(author=self.cleaned_data['author'],
                                       name=self.cleaned_data['name'],
                                       image=self.cleaned_data['image'],
                                       year_publication=self.cleaned_data['year_publication'],
                                       price=self.cleaned_data['price'],
                                       discount=self.cleaned_data['discount'],
                                       price_sale=self.cleaned_data['price_sale']
                                       )
        return new_b