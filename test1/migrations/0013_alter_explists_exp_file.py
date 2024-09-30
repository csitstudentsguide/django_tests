# Generated by Django 3.2.25 on 2024-09-30 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0012_alter_explists_exp_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explists',
            name='exp_file',
            field=models.FileField(upload_to='exp_lists/%Y/%m', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
