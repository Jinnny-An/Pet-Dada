# Generated by Django 3.1.3 on 2022-01-26 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_remove_review_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
