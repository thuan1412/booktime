# Generated by Django 2.2.7 on 2019-12-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productimage_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
