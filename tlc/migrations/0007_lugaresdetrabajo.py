# Generated by Django 3.1.7 on 2021-03-28 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlc', '0006_operador'),
    ]

    operations = [
        migrations.CreateModel(
            name='LugaresDeTrabajo',
            fields=[
                ('id_Lugar_asignado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ubicacion', models.CharField(max_length=50)),
                ('cantidad_total_lugares', models.IntegerField(max_length=3)),
                ('ubicacion', models.CharField(max_length=50)),
                ('cantidad_restante_lugares', models.IntegerField(max_length=3)),
            ],
        ),
    ]
