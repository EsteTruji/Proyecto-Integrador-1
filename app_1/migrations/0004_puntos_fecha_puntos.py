# Generated by Django 4.0.6 on 2022-09-08 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_actividad_etiqueta_puntos_residuo_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntos',
            name='fecha_puntos',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]