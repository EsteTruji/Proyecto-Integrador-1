# Generated by Django 4.0.6 on 2022-10-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_remove_etiqueta_etiqueta_etiqueta_bottle_cap_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='total_puntos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='etiqueta',
            name='Bottle_cap',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
