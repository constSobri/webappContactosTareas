# Generated by Django 4.2.1 on 2023-06-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
