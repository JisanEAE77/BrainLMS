# Generated by Django 3.2.4 on 2021-07-08 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0005_alter_instructorprofile_dp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructorprofile',
            old_name='student',
            new_name='instructor',
        ),
    ]
