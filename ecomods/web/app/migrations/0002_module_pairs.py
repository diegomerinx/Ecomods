# Generated by Django 4.2.7 on 2023-12-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='pairs',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
