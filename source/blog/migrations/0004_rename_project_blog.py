# Generated by Django 3.2.7 on 2021-09-27 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210927_2211'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Blog',
        ),
    ]
