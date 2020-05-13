# Generated by Django 3.0.6 on 2020-05-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posted', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, to='posted.Category'),
        ),
    ]
