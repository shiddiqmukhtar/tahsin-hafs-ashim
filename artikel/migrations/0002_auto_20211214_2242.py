# Generated by Django 3.2.9 on 2021-12-14 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='publish',
            new_name='published',
        ),
        migrations.RenameField(
            model_name='artikel',
            old_name='update',
            new_name='updated',
        ),
    ]
