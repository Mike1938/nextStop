# Generated by Django 4.2.5 on 2023-09-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_places_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='completed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
