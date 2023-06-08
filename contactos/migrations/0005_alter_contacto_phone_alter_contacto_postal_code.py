# Generated by Django 4.2.1 on 2023-06-05 22:31

import contactos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0004_alter_contacto_phone_alter_contacto_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='phone',
            field=models.CharField(max_length=15, validators=[contactos.models.validate_only_numbers]),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='postal_code',
            field=models.CharField(max_length=50, validators=[contactos.models.validate_only_numbers]),
        ),
    ]