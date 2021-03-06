# Generated by Django 3.1 on 2020-12-28 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_auto_20201228_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='favorite',
        ),
        migrations.AddField(
            model_name='favorites',
            name='username',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='usernames', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Me',
        ),
    ]
