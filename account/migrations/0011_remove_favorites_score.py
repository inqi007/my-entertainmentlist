# Generated by Django 3.1 on 2020-12-28 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20201228_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='score',
        ),
    ]