# Generated by Django 3.2 on 2023-05-10 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='posts',
        ),
    ]