# Generated by Django 3.2.5 on 2022-01-27 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
