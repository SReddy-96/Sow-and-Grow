# Generated by Django 5.0.6 on 2024-05-17 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_comments_harvest_harvest_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tending',
            old_name='end_month',
            new_name='end_transfer_month',
        ),
        migrations.RenameField(
            model_name='tending',
            old_name='start_month',
            new_name='start_transfer_month',
        ),
    ]
