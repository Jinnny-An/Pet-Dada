# Generated by Django 3.2.5 on 2022-01-26 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypageapp', '0009_alter_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_img',
            field=models.ImageField(blank=True, null=True, upload_to='pet_img'),
        ),
    ]
