# Generated by Django 5.0.7 on 2024-07-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_ad_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
    ]
