# Generated by Django 4.1.7 on 2023-03-08 21:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traine', models.CharField(max_length=50)),
                ('name', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]