# Generated by Django 3.2 on 2021-04-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=75)),
                ('telefono', models.CharField(max_length=12)),
                ('edad', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.TextField(max_length=75)),
            ],
        ),
    ]
