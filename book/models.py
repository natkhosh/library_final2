from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads')
    year_publication = models.CharField(max_length=4)
    price = models.CharField(max_length=10)
    discount = models.CharField(max_length=10, blank=True, null=True)
    price_sale = models.CharField(max_length=10, blank=True, null=True)



    def __str__(self):
        return f'{self.id} - {self.author} - {self.name}'
