# Generated by Django 3.1.3 on 2022-01-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20220125_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
    ]
