# Generated by Django 3.2.5 on 2022-02-05 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_user_add_somthing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='add_somthing',
        ),
    ]
