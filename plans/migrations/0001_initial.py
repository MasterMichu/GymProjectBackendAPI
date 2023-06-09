# Generated by Django 4.1.7 on 2023-03-13 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvilableExcercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Musclesgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('excercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.avilableexcercises')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traninglog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField()),
                ('weight', models.FloatField()),
                ('date', models.DateField()),
                ('excercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.avilableexcercises')),
                ('fromplan', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='plans.plans')),
            ],
        ),
        migrations.AddField(
            model_name='avilableexcercises',
            name='musclesgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.musclesgroup'),
        ),
    ]
