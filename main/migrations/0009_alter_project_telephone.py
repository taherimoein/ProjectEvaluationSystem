# Generated by Django 3.2 on 2021-06-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210614_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='telephone',
            field=models.CharField(max_length=11, verbose_name='شماره تماس'),
        ),
    ]
