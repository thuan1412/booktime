# Generated by Django 2.2.7 on 2019-12-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_date_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttag',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.ProductTag'),
        ),
    ]
