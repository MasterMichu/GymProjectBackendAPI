# Generated by Django 4.1.7 on 2023-03-31 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0006_remove_plans_name_planname_plans_planname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans',
            name='planname',
        ),
    ]
