# Generated by Django 3.2.13 on 2022-05-13 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perziura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='klientas',
            name='ivykdytas',
            field=models.BooleanField(default=False),
        ),
    ]
