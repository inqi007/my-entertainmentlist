# Generated by Django 3.1 on 2020-12-28 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20201228_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='towatch',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
    ]