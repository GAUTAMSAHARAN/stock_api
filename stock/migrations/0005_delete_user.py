# Generated by Django 3.1 on 2020-08-16 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]