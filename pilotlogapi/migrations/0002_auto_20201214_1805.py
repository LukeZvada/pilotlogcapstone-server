# Generated by Django 3.1.4 on 2020-12-14 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlogapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newlog',
            old_name='PilotUserId',
            new_name='PilotLogUserId',
        ),
    ]
