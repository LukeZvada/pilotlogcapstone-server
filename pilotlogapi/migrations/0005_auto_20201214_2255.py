# Generated by Django 3.1.4 on 2020-12-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlogapi', '0004_auto_20201214_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newlog',
            name='date',
            field=models.DateField(),
        ),
    ]
