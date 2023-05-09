# Generated by Django 4.1.7 on 2023-03-19 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plans', '0003_alter_avilableexcercises_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traninglog',
            name='fromplan',
        ),
        migrations.AddField(
            model_name='traninglog',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
