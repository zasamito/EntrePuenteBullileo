# Generated by Django 4.2.16 on 2024-11-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hostalhabitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('habitacion', models.TextField(max_length=35)),
                ('descripcion', models.TextField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]