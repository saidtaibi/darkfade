# Generated by Django 4.2 on 2023-05-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rondez_vous', '0003_rename_description_coupe_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupe',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
