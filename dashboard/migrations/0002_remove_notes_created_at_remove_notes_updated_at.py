# Generated by Django 5.0.3 on 2024-05-18 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='updated_at',
        ),
    ]
