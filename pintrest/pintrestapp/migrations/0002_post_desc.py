# Generated by Django 4.1.5 on 2023-01-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pintrestapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
