# Generated by Django 5.0.6 on 2024-05-20 10:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_end_month_tending_end_transfer_month_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_year', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='plantingyear',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planting_year', to='app.useryear'),
        ),
        migrations.AlterField(
            model_name='yearreview',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='year_reviews', to='app.useryear'),
        ),
    ]
