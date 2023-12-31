# Generated by Django 4.1.5 on 2023-01-19 12:31

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('uploadby', models.CharField(max_length=40)),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pintrestapp.tag')),
            ],
        ),
    ]
