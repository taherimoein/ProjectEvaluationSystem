from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.dateparse import parse_date, parse_datetime
from django.shortcuts import reverse
from datetime import datetime, date
from django.utils import timezone
from main.models import User
from django import template
import jdatetime

register = template.Library()

# -------------------------------------------------------------------------------------------------------------------------------------

def currency(value):
    return '{:,}'.format(int(value))
register.filter('currency', currency)

@register.simple_tag
def get_today_to_str(request):
    # month
    month = {
        1: 'فروردین',
        2: 'اردیبهشت',
        3: 'خرداد',
        4: 'تیر',
        5: 'مرداد',
        6: 'شهریور',
        7: 'مهر',
        8: 'آبان',
        9: 'آذر',
        10: 'دی',
        11: 'بهمن',
        12: 'اسفند'
    }
    # get date to str
    today = jdatetime.date.today()
    today_to_str = today.j_weekdays_fa[today.weekday()] + ' ' + str(today.day) + ' ' + month[today.month] + ' ' + str(today.year)
    return today_to_str
register.filter('get_today_to_str', get_today_to_str)

def string_to_jalali_date(value):
    try:
        date_format = "%Y-%m-%d"
        thisdate = datetime.strptime(str(parse_date(value)), date_format)
        return jdatetime.date.fromgregorian(day = thisdate.day, month = thisdate.month, year = thisdate.year).strftime("%Y/%m/%d")
    except:
        return 'ندارد'
register.filter('str_to_jalali_date', string_to_jalali_date)

def string_to_jalali_datetime(value):
    date_format = "%Y-%m-%d"
    thisdate = datetime.strptime(str(parse_datetime(value).date()), date_format)
    return jdatetime.date.fromgregorian(day = thisdate.day, month = thisdate.month, year = thisdate.year).strftime("%Y/%m/%d")
register.filter('str_to_jalali_datetime', string_to_jalali_datetime)

def gregorian_to_jalali_date(value):
    date_format = "%Y-%m-%d"
    thisdate = datetime.strptime(str(value), date_format)
    return jdatetime.date.fromgregorian(day = thisdate.day, month = thisdate.month, year = thisdate.year).strftime("%Y/%m/%d")
register.filter('date_to_jalali', gregorian_to_jalali_date)

def gregorian_to_jalali_datetime(value):
    date_format = "%Y-%m-%d"
    thisdate = datetime.strptime(str(value.date()), date_format)
    return jdatetime.date.fromgregorian(day = thisdate.day, month = thisdate.month, year = thisdate.year).strftime("%Y/%m/%d")
register.filter('datetime_to_jalali', gregorian_to_jalali_datetime)

def access_group_to_fa(value):
    if value is not None:
        access_group = {
            'user': 'کاربر',
            'department_of_administration': 'ریاست اداره',
            'deputy_for_planning_and_civil_affairs': 'معاونت امور برنامه ریزی و عمرانی',
            'governor': 'فرماندار'
        }
        return access_group[value]
    else:
        return 'ندارد'
register.filter('access_group_to_fa', access_group_to_fa)

def active_to_fa(value):
    active = {
        True: 'فعال',
        False: 'غیرفعال'
    }
    return active[value]
register.filter('active_to_fa', active_to_fa)

def gender_to_fa(value):
    try:
        gender = {
            'm': 'مرد',
            'f': 'زن'
        }
        return gender[value]
    except:
        return 'ندارد'
register.filter('gender_to_fa', gender_to_fa)

def degree_to_fa(value):
    try:
        degree = {
            'elementary': 'ابتدایی',
            'middle-school': 'سیکل',
            'diploma': 'دیپلم',
            'associate': 'فوق دیپلم',
            'bachelor': 'لیسانس',
            'master': 'فوق لیسانس',
            'phd': 'دکترا',
            'post-doctoral': 'فوق دکترا'
        }
        return degree[value]
    except:
        return 'ندارد'
register.filter('degree_to_fa', degree_to_fa)

def letter_status_to_fa(value):
    status = {
        0: 'خوانده نشده',
        1: 'خوانده شده',
        2: 'پاسخ داده شده',
        3: 'دیدن پاسخ'
    }
    return status[value]
register.filter('letter_status_to_fa', letter_status_to_fa)