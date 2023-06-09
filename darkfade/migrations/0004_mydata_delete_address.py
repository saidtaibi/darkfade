# Generated by Django 4.2 on 2023-05-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darkfade', '0003_address_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=2000, null=True)),
                ('link', models.CharField(max_length=3000, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=300, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
