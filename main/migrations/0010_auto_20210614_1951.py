# Generated by Django 3.2 on 2021-06-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_project_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='equal_distribution_credits_between_executive_devices',
            field=models.JSONField(blank=True, null=True, verbose_name='توزیع مساوی اعتبارات بین دستگاه های اجرایی '),
        ),
        migrations.AlterField(
            model_name='project',
            name='evaluation_user',
            field=models.JSONField(blank=True, null=True, verbose_name='ارزیابی کاربر'),
        ),
    ]
