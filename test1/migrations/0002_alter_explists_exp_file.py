# Generated by Django 5.1.1 on 2024-09-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explists',
            name='exp_file',
            field=models.FileField(upload_to='exp_lists/%Y/%m/%d'),
        ),
    ]
