# Generated by Django 4.2.3 on 2023-07-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_ugol_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ugol',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]