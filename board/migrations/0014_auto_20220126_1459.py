# Generated by Django 3.1.3 on 2022-01-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20220126_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
