# Generated by Django 3.0.2 on 2022-01-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypageapp', '0016_alter_pet_pet_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
