# Generated by Django 3.2.5 on 2022-01-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypageapp', '0010_alter_pet_pet_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_img',
            field=models.FileField(blank=True, null=True, upload_to='pet_img'),
        ),
    ]