# Generated by Django 4.0.3 on 2022-05-08 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perziura', '0019_alter_metai_marke_alter_metai_metai_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metai',
            old_name='marke',
            new_name='modelis',
        ),
        migrations.RenameField(
            model_name='spalva',
            old_name='marke',
            new_name='modelis',
        ),
    ]
