# Generated by Django 4.0.3 on 2022-05-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perziura', '0020_rename_marke_metai_modelis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metai',
            name='metai',
            field=models.CharField(blank=True, default='None', max_length=20, null=True, verbose_name='metai'),
        ),
        migrations.AlterField(
            model_name='spalva',
            name='spalva',
            field=models.CharField(blank=True, default='None', max_length=20, null=True, verbose_name='spalva'),
        ),
    ]
