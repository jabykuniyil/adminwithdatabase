# Generated by Django 3.1.5 on 2021-01-21 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_delete_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
