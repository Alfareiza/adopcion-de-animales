# Generated by Django 3.2 on 2021-04-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='comentarios',
            field=models.CharField(max_length=100),
        ),
    ]
