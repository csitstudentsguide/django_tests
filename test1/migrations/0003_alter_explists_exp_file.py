# Generated by Django 5.1.1 on 2024-09-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_alter_explists_exp_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explists',
            name='exp_file',
            field=models.FileField(upload_to='exp_lists/<django.db.models.fields.CharField>/'),
        ),
    ]
