# Generated by Django 4.1.7 on 2023-03-09 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Trainer', '0002_rename_trainerperson_trainers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainers',
            name='traine',
        ),
        migrations.AddField(
            model_name='trainers',
            name='methodsdescription',
            field=models.CharField(default='no description provided', max_length=1000),
        ),
        migrations.CreateModel(
            name='Gymgoer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goaldescription', models.CharField(default='no description provided', max_length=1000)),
                ('name', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gymconnetion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acceptance', models.BooleanField(default=False)),
                ('gymusername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trainer.gymgoer')),
                ('trainername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trainer.trainers')),
            ],
        ),
    ]
