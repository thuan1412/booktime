# Generated by Django 2.2.7 on 2019-12-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_productimage_producttag'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='', verbose_name='product-thumbnails'),
        ),
    ]