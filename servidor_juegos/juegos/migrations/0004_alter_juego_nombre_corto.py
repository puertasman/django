# Generated by Django 5.0.3 on 2024-03-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0003_alter_juego_nombre_corto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='nombre_corto',
            field=models.CharField(default='empty', max_length=100),
        ),
    ]
