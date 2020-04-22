# Generated by Django 3.0.3 on 2020-04-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads')),
                ('year_publication', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
                ('discount', models.CharField(blank=True, max_length=10, null=True)),
                ('price_sale', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
