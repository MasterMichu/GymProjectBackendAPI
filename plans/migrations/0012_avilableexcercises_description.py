# Generated by Django 4.1.7 on 2023-05-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0011_musclesgroup_image_alter_avilableexcercises_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='avilableexcercises',
            name='description',
            field=models.CharField(default='xdddd', max_length=3000),
            preserve_default=False,
        ),
    ]