from django.utils.dateparse import parse_datetime, parse_date
from django.db.models.functions import Concat
from django.http import JsonResponse
from django.db.models import Value
from django.utils import timezone
import re, json, pytz, kavenegar
from datetime import datetime

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def is_valid_national_code(input):
    if not re.search(r'^\d{10}$', input):
        return False

    if re.search(r'^([0-9])\1{9}$', input):
        return False

    check = int(input[9])
    s = sum([int(input[x]) * (10 - x) for x in range(9)]) % 11
    return (s < 2 and check == s) or (s >= 2 and check + s == 11)


# check password (password must be at least 8 characters - including lowercase letters and numbers)
def check_password(password, repeat_password):
    password_pattern = r'^[A-Za-z0-9@#$%^&+=!()\-\_\.\*\\\/\[\]\{\}?,~`]{8,}$'
    if password == repeat_password:
        if (re.search(password_pattern, password)) and (re.search(password_pattern, repeat_password)):
            return True, None
        else:
            return False, 'رمز عبور و تکرار آن مطابق الگو نمی باشند.'
    else:
        return False, 'رمز عبور و تکرار آن یکسان نمی باشند.'


def calculate_date_difference(start_date, end_date):
    date_format = "%Y-%m-%d"
    start = datetime.strptime(str(start_date), date_format)
    end = datetime.strptime(str(end_date), date_format)
    delta = end - start
    return delta.days


def calculate_time_difference(start_time, end_time):
    date_format = "%Y-%m-%d %H:%M:%S.%f%z"
    start = datetime.strptime(str(start_time), date_format)
    end = datetime.strptime(str(end_time), date_format)
    delta = end - start
    return delta.seconds


def send_sms(to_number, template, verify_code):
    try:
        api = kavenegar.KavenegarAPI('2B485230622F74625978584E343167657576785041736B4A586D6E524C4661577A56566B44366D674C75413D')
        params = {
            'receptor': to_number,
            'template': template,
            'token': verify_code,
            'type': 'sms',
        }
        api.verify_lookup(params)
        return True, None
    except Exception as e:
        return False, str(e)


def convert_to_regex(this_text):
    # set regex
    text = this_text.split(' ')
    text = list(filter(lambda i: i != '', text))
    word_list = []
    for word in text:
        result_word = list(map(lambda x: x + '\s*', word.replace(' ','')[:-1]))
        result_word = ''.join(result_word) + word[-1]
        word_list.append(result_word)
    result_word = r'.*'.join(word_list)
    return result_word