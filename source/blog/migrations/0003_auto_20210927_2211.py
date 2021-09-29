# Generated by Django 3.2.7 on 2021-09-27 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_projects_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
