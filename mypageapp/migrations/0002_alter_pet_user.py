# Generated by Django 3.2.5 on 2022-01-26 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mypageapp.user', unique=True),
        ),
    ]