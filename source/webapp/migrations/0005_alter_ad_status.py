# Generated by Django 5.0.7 on 2024-07-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_ad_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='status',
            field=models.CharField(choices=[('1', 'Moderate'), ('2', 'Approve'), ('3', 'Rejection'), ('4', 'On delete')], default=1, max_length=30, verbose_name='Category'),
        ),
    ]
