# Generated by Django 4.0.1 on 2022-02-02 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_myuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='myuser',
        ),
        migrations.DeleteModel(
            name='myuser1',
        ),
    ]
