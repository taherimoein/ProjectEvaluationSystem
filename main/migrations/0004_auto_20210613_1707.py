# Generated by Django 3.2 on 2021-06-13 12:37

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='history',
            field=models.JSONField(default=main.models.default_history_field(), verbose_name='تاریخچه'),
        ),
        migrations.AlterField(
            model_name='project',
            name='type_of_financial_resources',
            field=models.TextField(verbose_name='نوع منابع مالی'),
        ),
    ]
