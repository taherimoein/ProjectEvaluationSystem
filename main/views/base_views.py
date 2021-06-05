from utils.base_fuction import is_valid_national_code, check_password, send_sms, calculate_time_difference
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
import datetime, json, random, string, re
from django.http import JsonResponse
from django.utils import timezone
from django.conf import settings
# get model
from main.models import User, Validation

# -------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url = 'main:sign_page')
def index_page(request):
    return render(request, 'main/index.html')


def signin_page(request):
    if not request.user.is_authenticated:
        return render(request, 'account/signin.html')
    else:
        return redirect('main:index_page')


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main:index_page')
    else:
        return redirect('main:index_page')


def signin(request):
    response_data = {}
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = json.loads(request.POST.get('remember_me'))
        # get this user
        user = authenticate(request, username = username, password = password)
        # check user
        if user is not None:
            # login user
            login(request, user)
            if remember_me:
                session_key = request.session.session_key or Session.objects.get_new_session_key()
                Session.objects.save(session_key, request.session._session, timezone.now() + datetime.timedelta(seconds = settings.SESSION_COOKIE_AGE))

            response_data['status'] = '200'
            return JsonResponse(response_data)
        else:
            response_data['status'] = '404'
            response_data['error'] = 'نام کاربری یا رمز عبور اشتباه است و یا حساب کاربری شما غیر فعال شده است.'
            return JsonResponse(response_data)
    except Exception as e:
        response_data['status'] = '500'
        response_data['error'] = str(e)
        return JsonResponse(response_data)


def forget_password_page(request):
    if not request.user.is_authenticated:
        return render(request, 'account/forget-password.html')
    else:
        return redirect('main:index_page')


def forget_password_send_validation_code(request):
    response_data = {}
    try:
        if not request.user.is_authenticated:
            # get data
            this_mobile = request.POST.get('mobile')
            # check mobile
            if User.objects.filter(mobile = this_mobile).exists():
                this_user = User.objects.get(mobile = this_mobile)
                # check mobile in Validation Model
                if Validation.objects.filter(mobile = this_mobile).exists():
                    this_validation = Validation.objects.get(mobile = this_mobile)
                    # check send time
                    start = timezone.localtime(this_validation.createdatetime)
                    end = timezone.localtime(timezone.now())
                    delta_time = calculate_time_difference(start, end)
                    if delta_time <= 120:
                        response_data['status'] = '400'
                        response_data['error'] = 'کد ارسال شده برای شما هنوز معتبر می باشد.'
                        return JsonResponse(response_data)
                    else:
                        this_validation.validation_code = ''.join(random.choice(string.digits) for i in range(6))
                        this_validation.createdatetime = timezone.now()
                        this_validation.save()
                        status, error = send_sms(this_mobile, 'hse-verify-code', str(this_validation.validation_code))
                        response_data['status'] = '200'
                        response_data['send_sms_status'] = {'status': status, 'error': error}
                        response_data['user_id'] = this_user.id
                        return JsonResponse(response_data)
                else:
                    this_validation = Validation.objects.create(mobile = this_mobile)
                    status, error = send_sms(this_mobile, 'hse-verify-code', str(this_validation.validation_code))
                    response_data['status'] = '201'
                    response_data['send_sms_status'] = {'status': status, 'error': error}
                    response_data['user_id'] = this_user.id
                    return JsonResponse(response_data)
            else:
                response_data['status'] = '404'
                response_data['error'] = 'کاربری با این شماره موبایل در سیستم موجود نمی باشد.'
                return JsonResponse(response_data)
        else:
            response_data['status'] = '400'
            response_data['error'] = 'شما در حال حاضر نمی توانید از فراموشی رمز عبور استفاده کنید.'
            return JsonResponse(response_data)
    except Exception as e:
        response_data['status'] = '500'
        response_data['error'] = str(e)
        return JsonResponse(response_data)


def forget_password_change_password(request):
    response_data = {}
    try:
        if not request.user.is_authenticated:
            # get data
            this_user_id = request.POST.get('user_id')
            this_validation_code = request.POST.get('validation_code')
            this_password = request.POST.get('password')
            this_re_password = request.POST.get('re_password')
            # set data
            this_user = User.objects.get(id = this_user_id)
            # check mobile
            if Validation.objects.filter(mobile = this_user.mobile).exists():
                this_validation = Validation.objects.get(mobile = this_user.mobile)
                # check send time
                start = timezone.localtime(this_validation.createdatetime)
                end = timezone.localtime(timezone.now())
                delta_time = calculate_time_difference(start, end)
                if delta_time > 120:
                    response_data['status'] = '406'
                    response_data['error'] = 'کد وارد شده، منقضی شده است.'
                    return JsonResponse(response_data)
                # check validation code
                if this_validation.validation_code == this_validation_code:
                    password_status, error = check_password(this_password, this_re_password)
                    if not password_status:
                        response_data['status'] = '400'
                        response_data['error'] = error
                        return JsonResponse(response_data)
                    # change password
                    this_user.set_password(this_password)
                    this_user.save()
                    
                    response_data['status'] = '200'
                    return JsonResponse(response_data)
                else:
                    response_data['status'] = '406'
                    response_data['error'] = 'کد وارد شده درست نمی باشد.'
                    return JsonResponse(response_data)
            else:
                response_data['status'] = '404'
                response_data['error'] = 'کدی برای این کاربر ارسال نشده است.'
                return JsonResponse(response_data)
        else:
            response_data['status'] = '400'
            response_data['error'] = 'شما در حال حاضر نمی توانید از فراموشی رمز عبور استفاده کنید.'
            return JsonResponse(response_data)
    except Exception as e:
        response_data['status'] = '500'
        response_data['error'] = str(e)
        return JsonResponse(response_data)