# Generated by Django 5.0.7 on 2024-07-24 06:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_appuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='phone',
            field=models.CharField(default=66, max_length=16, validators=[django.core.validators.MinLengthValidator(16)], verbose_name='Phone number'),
            preserve_default=False,
        ),
    ]
