# Generated by Django 4.2 on 2023-05-02 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rondez_vous', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='coupe',
        ),
        migrations.AddField(
            model_name='coupe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_coupe', to='rondez_vous.category'),
        ),
    ]
