# Generated by Django 3.2.4 on 2021-07-10 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackorder', '0003_auto_20210710_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gigorder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tutionsubscriptionorder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]