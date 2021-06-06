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


def signup_page(request):
    if not request.user.is_authenticated:
        return render(request, 'account/signup.html')
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


def check_signup_fields(request):
    try:
        # get data
        this_username = request.POST.get('username')
        this_password = request.POST.get('password')
        this_first_name = request.POST.get('first_name')
        this_last_name = request.POST.get('last_name')
        this_father_s_name = request.POST.get('father_s_name')
        this_gender = request.POST.get('gender')
        this_birth_certificate_id = request.POST.get('birth_certificate_id')
        this_national_code = request.POST.get('national_code')
        this_birthday = request.POST.get('birthday')
        this_issue_place = request.POST.get('issue_place')
        this_degree = request.POST.get('degree')
        this_major = request.POST.get('major')
        this_university_of_study = request.POST.get('university_of_study')
        this_executive_device = request.POST.get('executive_device')
        this_role = request.POST.get('role')
        this_work_experience = request.POST.get('work_experience')
        this_personnel_id = request.POST.get('personnel_id')
        this_address = request.POST.get('address')
        this_zip_code = request.POST.get('zip_code')
        this_mobile = request.POST.get('mobile')
        this_necessary_contact_number = request.POST.get('necessary_contact_number')
        this_workplace_number = request.POST.get('workplace_number')
        this_email = request.POST.get('email')
        this_profile = request.FILES['profile']
        this_picture = request.FILES['picture']
        this_personal_id_card = request.FILES['personal_id_card']
        this_device_introduction_letter = request.FILES['device_introduction_letter']
        this_sample_signature = request.FILES['sample_signature']
        # check duplicate data
        if User.objects.filter(username = this_username).exists():
            return False, 'کاربری با این نام کاربری در سیستم موجود می باشد.'
        if User.objects.filter(birth_certificate_id = this_birth_certificate_id).exists():
            return False, 'کاربری با این شمماره شناسنامه در سیستم موجود می باشد.'
        if User.objects.filter(national_code = this_national_code).exists():
            return False, 'کاربری با این کدملی در سیستم موجود می باشد.'
        if User.objects.filter(mobile = this_mobile).exists():
            return False, 'کاربری با این شماره موبایل در سیستم موجود می باشد.'
        if User.objects.filter(personnel_id = this_personnel_id).exists():
            return False, 'کاربری با این شماره پرسنلی در سیستم موجود می باشد.'
        if User.objects.filter(email = this_email).exists():
            return False, 'کاربری با این پست الکترونیکی در سیستم موجود می باشد.'

        return True, None
    except:
        return False, 'همه داده های مورد نیاز به درستی ارسال نشده است.'


def signup(request):
    response_data = {}
    try:
        check_data_status, error = check_signup_fields(request)
        if not check_data_status:
            response_data['status'] = '400'
            response_data['error'] = error
            return JsonResponse(response_data)
        # get data
        this_username = request.POST.get('username')
        this_password = request.POST.get('password')
        this_first_name = request.POST.get('first_name')
        this_last_name = request.POST.get('last_name')
        this_father_s_name = request.POST.get('father_s_name')
        this_gender = request.POST.get('gender')
        this_birth_certificate_id = request.POST.get('birth_certificate_id')
        this_national_code = request.POST.get('national_code')
        this_birthday = request.POST.get('birthday')
        this_issue_place = request.POST.get('issue_place')
        this_degree = request.POST.get('degree')
        this_major = request.POST.get('major')
        this_university_of_study = request.POST.get('university_of_study')
        this_executive_device = request.POST.get('executive_device')
        this_role = request.POST.get('role')
        this_work_experience = request.POST.get('work_experience')
        this_personnel_id = request.POST.get('personnel_id')
        this_address = request.POST.get('address')
        this_zip_code = request.POST.get('zip_code')
        this_mobile = request.POST.get('mobile')
        this_necessary_contact_number = request.POST.get('necessary_contact_number')
        this_workplace_number = request.POST.get('workplace_number')
        this_email = request.POST.get('email')
        this_profile = request.FILES['profile']
        this_picture = request.FILES['picture']
        this_personal_id_card = request.FILES['personal_id_card']
        this_device_introduction_letter = request.FILES['device_introduction_letter']
        this_sample_signature = request.FILES['sample_signature']
        # create new user
        this_user = User.objects.create_user(this_username, this_first_name, this_last_name,\
            this_father_s_name, this_birth_certificate_id, this_national_code)
        # add other fields
        this_user.set_password(this_password)
        this_user.gender = this_gender
        this_user.birth_certificate_id = this_birth_certificate_id
        this_user.national_code = this_national_code
        this_user.birthday = this_birthday
        this_user.issue_place = this_issue_place
        this_user.degree = this_degree
        this_user.major = this_major
        this_user.university_of_study = this_university_of_study
        this_user.executive_device = this_executive_device
        this_user.role = this_role
        this_user.work_experience = this_work_experience
        this_user.personnel_id = this_personnel_id
        this_user.address = this_address
        this_user.zip_code = this_zip_code
        this_user.mobile = this_mobile
        this_user.necessary_contact_number = this_necessary_contact_number
        this_user.workplace_number = this_workplace_number
        this_user.email = this_email
        this_user.profile = this_profile
        this_user.picture = this_picture
        this_user.personal_id_card = this_personal_id_card
        this_user.device_introduction_letter = this_device_introduction_letter
        this_user.sample_signature = this_sample_signature
        this_user.active = False
        this_user.save()
        this_user.add_history('create', None)

        response_data['status'] = '201'
        return JsonResponse(response_data)
    except Exception as e:
        response_data['status'] = '500'
        response_data['error'] = str(e)
        return JsonResponse(response_data)