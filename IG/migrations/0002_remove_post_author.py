# Generated by Django 3.0.6 on 2020-05-11 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IG', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
