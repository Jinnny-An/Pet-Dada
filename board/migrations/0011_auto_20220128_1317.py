# Generated by Django 3.2.5 on 2022-01-28 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_auto_20220128_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]