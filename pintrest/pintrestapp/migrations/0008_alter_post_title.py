# Generated by Django 4.1.5 on 2023-01-27 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pintrestapp', '0007_alter_like_post_alter_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
