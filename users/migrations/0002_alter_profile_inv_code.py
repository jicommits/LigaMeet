# Generated by Django 5.0.1 on 2024-10-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='INV_CODE',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
