# Generated by Django 3.2.4 on 2021-07-08 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instructor', '0003_alter_subscriptiontype_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(upload_to='student_dp')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.subject')),
            ],
        ),
    ]
