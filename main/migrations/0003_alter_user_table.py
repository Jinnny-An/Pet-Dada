# Generated by Django 3.2.5 on 2022-01-27 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220127_1616'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='user_main',
        ),
    ]