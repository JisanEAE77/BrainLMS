# Generated by Django 3.2.4 on 2021-07-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_subscriptiontype_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptiontype',
            name='slug',
            field=models.CharField(max_length=100),
        ),
    ]
