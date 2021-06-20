# Generated by Django 3.2 on 2021-06-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210614_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executive_Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=3, verbose_name='کد')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='عنوان')),
                ('year', models.CharField(max_length=4, verbose_name='سال')),
                ('address_general_administration', models.TextField(blank=True, null=True, verbose_name='آدرس اداره کل')),
                ('telephone', models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره تلفن')),
                ('fax', models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره فاکس')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('website', models.URLField(blank=True, null=True, verbose_name='وب سایت')),
                ('boss_executive_device', models.JSONField(blank=True, null=True, verbose_name='ریاست دستگاه اجرایی')),
                ('assistance_executive_device', models.JSONField(blank=True, null=True, verbose_name='معاونت دستگاه اجرایی')),
                ('number_employees', models.PositiveIntegerField(default=0, verbose_name='تعداد پرسنل استخدامی')),
                ('number_contract_staff', models.PositiveIntegerField(default=0, verbose_name='تعداد نیروی قراردادی')),
                ('number_buildings', models.PositiveIntegerField(default=0, verbose_name='تعداد ساختمان')),
                ('number_unreinforced_buildings', models.PositiveIntegerField(default=0, verbose_name='تعداد ساختمان های فاقد استحکام')),
                ('buildings', models.JSONField(blank=True, null=True, verbose_name='ساختمان های دستگاه اجرایی')),
                ('number_projects_last_year', models.PositiveIntegerField(default=0, verbose_name='تعداد پروژه های سال گذشته')),
                ('number_completed_financial_projects', models.PositiveIntegerField(default=0, verbose_name='تعداد پروژه های محقق شده مالی')),
                ('amount_budget_requested_last_year', models.BigIntegerField(default=0, verbose_name='میزان بودجه درخواستی سال گذشته')),
                ('budget_realized_last_year', models.BigIntegerField(default=0, verbose_name='بودجه محقق شده در سال گذشته')),
                ('amount_budget_allocated_last_year', models.BigIntegerField(default=0, verbose_name='میزان بودجه تخصیص یافته سال گذشته')),
                ('number_completed_projects', models.PositiveIntegerField(default=0, verbose_name='تعداد پروژه تکمیل یافته')),
                ('number_projects_remaining', models.PositiveIntegerField(default=0, verbose_name='تعداد پروژه های باقی مانده')),
                ('number_projects_is_behind_schedule', models.PositiveIntegerField(default=0, verbose_name='تعداد پروژه های از زمانبندی عقب تر است')),
                ('number_projects_not_been_completed_more_year', models.PositiveIntegerField(default=0, verbose_name='تعداد پروژه هایی که بیش از یکسال به اتمام نرسیده')),
                ('projects_behind_schedule', models.JSONField(blank=True, null=True, verbose_name='پروژه های غبت از زمان بندی')),
                ('projects_not_been_completed_more_year', models.JSONField(blank=True, null=True, verbose_name='پروژه های که بیش از یکسال اتمام نشده')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
            options={
                'verbose_name': 'دستگاه اجرایی',
                'verbose_name_plural': 'دستگاه های اجرایی',
                'ordering': ('id', 'create_date'),
            },
        ),
    ]