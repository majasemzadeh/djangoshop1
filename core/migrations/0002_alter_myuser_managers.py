# Generated by Django 4.0.5 on 2022-06-21 16:01

import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', core.models.MyUserManager()),
            ],
        ),
    ]