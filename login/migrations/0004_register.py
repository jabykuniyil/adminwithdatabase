# Generated by Django 3.1.5 on 2021-01-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=16)),
                ('lastname', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
