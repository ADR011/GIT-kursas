# Generated by Django 4.0.3 on 2022-05-07 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perziura', '0008_spalva_order_gimimo_data_alter_metai_metai_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metai',
            name='modeliai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metai', to='perziura.modelis'),
        ),
    ]