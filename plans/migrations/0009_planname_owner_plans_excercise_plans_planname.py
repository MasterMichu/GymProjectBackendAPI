# Generated by Django 4.1.7 on 2023-03-31 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plans', '0008_remove_planname_owner_remove_plans_excercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='planname',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plans',
            name='excercise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plans.avilableexcercises'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plans',
            name='planname',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plans.planname'),
            preserve_default=False,
        ),
    ]
