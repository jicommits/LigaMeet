# Generated by Django 5.0.7 on 2024-09-10 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='TYPE',
        ),
    ]
