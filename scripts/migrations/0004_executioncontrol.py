# Generated by Django 3.2.25 on 2025-03-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0003_executionrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Control de Ejecución',
                'verbose_name_plural': 'Controles de Ejecución',
            },
        ),
    ]
