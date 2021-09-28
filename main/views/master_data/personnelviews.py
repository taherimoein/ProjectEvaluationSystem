from main.serializers.master_data import UserBaseSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, get_object_or_404
from utils.decorators.access_level import is_governor
from utils.base_fuction import is_valid_national_code
from django.db.models.functions import Concat
from django.db.models import Value, Q
from django.http import JsonResponse
import json
# get model
from main.models import User

# -------------------------------------------------------------------------------------------------------------------------------------

@is_governor
@login_required(login_url = 'main:sign_page')
def personnel_list_page(request):
    users = User.objects.annotate(fullname = Concat('first_name', Value(' '), 'last_name')) \
        .order_by('create_date').values('id', 'national_code', 'fullname', 'father_s_name', \
            'role', 'executive_device', 'personnel_id', 'necessary_contact_number',\
            'mobile', 'username', 'access_group', 'active')

    context = {
        'Users': users
    }
    return render(request, 'master-data/personnel/personnel-list.html', context)


@is_governor
@login_required(login_url = 'main:sign_page')
def personnel_create_page(request):
    return render(request, 'master-data/personnel/personnel-create.html')


def check_personnel_fields(request):
    try:
        # get data
        this_username = request.POST.get('username')
        this_password = request.POST.get('password')
        this_first_name = request.POST.get('first_name')
        this_last_name = request.POST.get('last_name')
        this_father_s_name = request.POST.get('father_s_name')
        this_access_group = request.POST.get('access_group')
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


def create_personnel(request):
    response_data = {}
    if request.user.is_authenticated:
        try:
            check_data_status, error = check_personnel_fields(request)
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
            this_access_group = request.POST.get('access_group')
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
            this_user.access_group = this_access_group
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
            this_user.save()
            this_user.add_history('create', request.user.id)

            response_data['status'] = '201'
            return JsonResponse(response_data)
        except Exception as e:
            response_data['status'] = '500'
            response_data['error'] = str(e)
            return JsonResponse(response_data)
    else:
        response_data['status'] = '401'
        response_data['error'] = 'شما وارد سیستم نشده اید.'
        return JsonResponse(response_data)


def get_user_details(this_user):
    this_user_details = {
        'id': this_user.id,
        'national_code': this_user.national_code,
        'first_name': this_user.first_name,
        'last_name': this_user.last_name,
        'profile': this_user.profile,
        'father_s_name': this_user.father_s_name,
        'birth_certificate_id': this_user.birth_certificate_id,
        'birthday': this_user.birthday,
        'issue_place': this_user.issue_place,
        'gender': this_user.gender,
        'username': this_user.username,
        'major': this_user.major,
        'degree': this_user.degree,
        'necessary_contact_number': this_user.necessary_contact_number,
        'mobile': this_user.mobile,
        'address': this_user.address,
        'workplace_number': this_user.workplace_number,
        'role': this_user.role,
        'university_of_study': this_user.university_of_study,
        'executive_device': this_user.executive_device,
        'work_experience': this_user.work_experience,
        'personnel_id': this_user.personnel_id,
        'zip_code': this_user.zip_code,
        'email': this_user.email,
        'picture': this_user.picture,
        'personal_id_card': this_user.personal_id_card,
        'device_introduction_letter': this_user.device_introduction_letter,
        'sample_signature': this_user.sample_signature
    }
    return this_user_details


@is_governor
@login_required(login_url = 'main:sign_page')
def personnel_details_page(request, username):
    this_user = get_object_or_404(User, username = username)

    context = {
        'ThisUser': get_user_details(this_user)
    }
    return render(request, 'master-data/personnel/personnel-details.html', context)


@is_governor
@login_required(login_url = 'main:sign_page')
def personnel_edit_page(request, username):
    this_user = get_object_or_404(User, username = username)

    context = {
        'ThisUser': get_user_details(this_user)
    }
    return render(request, 'master-data/personnel/personnel-edit.html', context)


def check_personnel_fields_edit(request):
    try:
        # get data
        this_user = request.user
        this_username = request.POST.get('username')
        this_national_code = request.POST.get('national_code')
        this_birth_certificate_id = request.POST.get('birth_certificate_id')
        this_personnel_id = request.POST.get('personnel_id')
        this_mobile = request.POST.get('mobile')
        this_email = request.POST.get('email')
        # check duplicate data
        if this_user.username != this_username:
            if User.objects.filter(username = this_username).exists():
                return False, 'کاربری با این نام کاربری در سیستم موجود می باشد.'
        if this_user.birth_certificate_id != this_birth_certificate_id:
            if User.objects.filter(birth_certificate_id = this_birth_certificate_id).exists():
                return False, 'کاربری با این شمماره شناسنامه در سیستم موجود می باشد.'
        if this_user.national_code != this_national_code:
            if User.objects.filter(national_code = this_national_code).exists():
                return False, 'کاربری با این کدملی در سیستم موجود می باشد.'
        if this_user.mobile != this_mobile:
            if User.objects.filter(mobile = this_mobile).exists():
                return False, 'کاربری با این شماره موبایل در سیستم موجود می باشد.'
        if this_user.personnel_id != this_personnel_id:
            if User.objects.filter(personnel_id = this_personnel_id).exists():
                return False, 'کاربری با این شماره پرسنلی در سیستم موجود می باشد.'
        if this_user.email != this_email:
            if User.objects.filter(email = this_email).exists():
                return False, 'کاربری با این پست الکترونیکی در سیستم موجود می باشد.'

        return True, None
    except:
        return False, 'همه داده های مورد نیاز به درستی ارسال نشده است.'


def edit_personnel(request):
    response_data = {}
    if request.user.is_authenticated:
        try:
            check_data_status, error = check_personnel_fields_edit(request)
            if not check_data_status:
                response_data['status'] = '400'
                response_data['error'] = error
                return JsonResponse(response_data)
            # get data
            this_username = request.POST.get('username')
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
            try:
                this_profile = request.FILES['profile']
            except:
                this_profile = None
            try:
                this_picture = request.FILES['picture']
            except:
                this_picture = None
            try:
                this_personal_id_card = request.FILES['personal_id_card']
            except:
                this_personal_id_card = None
            try:
                this_device_introduction_letter = request.FILES['device_introduction_letter']
            except:
                this_device_introduction_letter = None
            try:
                this_sample_signature = request.FILES['sample_signature']
            except:
                this_sample_signature = None
            # get this user
            this_user = request.user
            # edit all fields
            edit_fields = []
            if this_user.username != this_username:
                edit_fields.append({'field_name': 'username', 'old_data': this_user.username, 'new_data': this_username})
                this_user.username = this_username
            if this_user.first_name != this_first_name:
                edit_fields.append({'field_name': 'first_name', 'old_data': this_user.first_name, 'new_data': this_first_name})
                this_user.first_name = this_first_name
            if this_user.last_name != this_last_name:
                edit_fields.append({'field_name': 'last_name', 'old_data': this_user.last_name, 'new_data': this_last_name})
                this_user.last_name = this_last_name
            if this_user.father_s_name != this_father_s_name:
                edit_fields.append({'field_name': 'father_s_name', 'old_data': this_user.father_s_name, 'new_data': this_father_s_name})
                this_user.father_s_name = this_father_s_name
            if this_user.birth_certificate_id != this_birth_certificate_id:
                edit_fields.append({'field_name': 'birth_certificate_id', 'old_data': this_user.birth_certificate_id, 'new_data': this_birth_certificate_id})
                this_user.birth_certificate_id = this_birth_certificate_id
            if this_user.national_code != this_national_code:
                edit_fields.append({'field_name': 'national_code', 'old_data': this_user.national_code, 'new_data': this_national_code})
                this_user.national_code = this_national_code
            if this_user.gender != this_gender:
                edit_fields.append({'field_name': 'gender', 'old_data': this_user.gender, 'new_data': this_gender})
                this_user.gender = this_gender
            if this_user.birthday != this_birthday:
                edit_fields.append({'field_name': 'birthday', 'old_data': this_user.birthday, 'new_data': this_birthday})
                this_user.birthday = this_birthday
            if this_user.issue_place != this_issue_place:
                edit_fields.append({'field_name': 'issue_place', 'old_data': this_user.issue_place, 'new_data': this_issue_place})
                this_user.issue_place = this_issue_place
            if this_user.degree != this_degree:
                edit_fields.append({'field_name': 'degree', 'old_data': this_user.degree, 'new_data': this_degree})
                this_user.degree = this_degree
            if this_user.major != this_major:
                edit_fields.append({'field_name': 'major', 'old_data': this_user.major, 'new_data': this_major})
                this_user.major = this_major
            if this_user.university_of_study != this_university_of_study:
                edit_fields.append({'field_name': 'university_of_study', 'old_data': this_user.university_of_study, 'new_data': this_university_of_study})
                this_user.university_of_study = this_university_of_study
            if this_user.executive_device != this_executive_device:
                edit_fields.append({'field_name': 'executive_device', 'old_data': this_user.executive_device, 'new_data': this_executive_device})
                this_user.executive_device = this_executive_device
            if this_user.role != this_role:
                edit_fields.append({'field_name': 'role', 'old_data': this_user.role, 'new_data': this_role})
                this_user.role = this_role
            if this_user.work_experience != this_work_experience:
                edit_fields.append({'field_name': 'work_experience', 'old_data': this_user.work_experience, 'new_data': this_work_experience})
                this_user.work_experience = this_work_experience
            if this_user.personnel_id != this_personnel_id:
                edit_fields.append({'field_name': 'personnel_id', 'old_data': this_user.personnel_id, 'new_data': this_personnel_id})
                this_user.personnel_id = this_personnel_id
            if this_user.address != this_address:
                edit_fields.append({'field_name': 'address', 'old_data': this_user.address, 'new_data': this_address})
                this_user.address = this_address
            if this_user.zip_code != this_zip_code:
                edit_fields.append({'field_name': 'zip_code', 'old_data': this_user.zip_code, 'new_data': this_zip_code})
                this_user.zip_code = this_zip_code
            if this_user.mobile != this_mobile:
                edit_fields.append({'field_name': 'mobile', 'old_data': this_user.mobile, 'new_data': this_mobile})
                this_user.mobile = this_mobile
            if this_user.necessary_contact_number != this_necessary_contact_number:
                edit_fields.append({'field_name': 'necessary_contact_number', 'old_data': this_user.necessary_contact_number, 'new_data': this_necessary_contact_number})
                this_user.necessary_contact_number = this_necessary_contact_number
            if this_user.workplace_number != this_workplace_number:
                edit_fields.append({'field_name': 'workplace_number', 'old_data': this_user.workplace_number, 'new_data': this_workplace_number})
                this_user.workplace_number = this_workplace_number
            if this_user.email != this_email:
                edit_fields.append({'field_name': 'email', 'old_data': this_user.email, 'new_data': this_email})
                this_user.email = this_email
            if this_profile != None:
                edit_fields.append({'field_name': 'profile', 'old_data': this_user.profile, 'new_data': this_profile})
                this_user.profile = this_profile
            if this_picture != None:
                edit_fields.append({'field_name': 'picture', 'old_data': this_user.picture, 'new_data': this_picture})
                this_user.picture = this_picture
            if this_personal_id_card != None:
                edit_fields.append({'field_name': 'personal_id_card', 'old_data': this_user.personal_id_card, 'new_data': this_personal_id_card})
                this_user.personal_id_card = this_personal_id_card
            if this_device_introduction_letter != None:
                edit_fields.append({'field_name': 'device_introduction_letter', 'old_data': this_user.device_introduction_letter, 'new_data': this_device_introduction_letter})
                this_user.device_introduction_letter = this_device_introduction_letter
            if this_sample_signature != None:
                edit_fields.append({'field_name': 'sample_signature', 'old_data': this_user.sample_signature, 'new_data': this_sample_signature})
                this_user.sample_signature = this_sample_signature

            this_user.save()
            # add edit history
            this_user.add_history('edit', request.user.id, edit_fields)

            response_data['status'] = '200'
            return JsonResponse(response_data)
        except Exception as e:
            response_data['status'] = '500'
            response_data['error'] = str(e)
            return JsonResponse(response_data)
    else:
        response_data['status'] = '401'
        response_data['error'] = 'شما وارد سیستم نشده اید.'
        return JsonResponse(response_data)


def search_in_users(request):
    response_data = {}
    try:
        # get search
        this_search = request.POST.get('search')
        # set search regex
        this_search = this_search.split(' ')
        this_search = list(filter(lambda i: i != '', this_search))
        search_word_list = []
        for word in this_search:
            search_word = list(map(lambda x: x + '\s*', word.replace(' ','')[:-1]))
            search_word = ''.join(search_word) + word[-1]
            search_word_list.append(search_word)
        search_word = r'.*'.join(search_word_list)
        # search in fullname & national_code
        users = User.objects.annotate(full_name = Concat('first_name', Value(' '), 'last_name')).filter(Q(full_name__regex = search_word) | Q(national_code__regex = search_word))
        serializer = UserBaseSerializer(users, many = True)

        response_data['status'] = '200'
        response_data['data'] = serializer.data
        return JsonResponse(response_data)
    except Exception as e:
        response_data['status'] = '500'
        response_data['error'] = str(e)
        return JsonResponse(response_data)


@is_governor
@login_required(login_url = 'main:sign_page')
def personnel_confirmation_of_information_page(request, username):
    this_user = get_object_or_404(User, username = username)

    context = {
        'ThisUser': get_user_details(this_user)
    }
    return render(request, 'master-data/personnel/personnel_confirmation_of_information.html', context)


def confirmation_of_information_personnel(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.is_governor:
            try:
                # get data
                this_user_id = request.POST.get('id')
                this_access_group = request.POST.get('access_group')

                if User.objects.filter(id = this_user_id).exists():
                    if this_access_group in ['user', 'department_of_administration']:
                        # get user 
                        this_user = User.objects.get(id = this_user_id)
                        # change user access group
                        this_user.access_group = this_access_group
                        this_user.active = True
                        this_user.save()
                        # add create history
                        this_user.add_history('confirmation', request.user.id, {'access_group': this_access_group})

                        response_data['status'] = '200'
                        return JsonResponse(response_data)
                    else:
                        response_data['status'] = '400'
                        response_data['error'] = 'اطلاعات به درستی ارسال نشده است.'
                        return JsonResponse(response_data)
                else:
                    response_data['status'] = '404'
                    response_data['error'] = f'کاربری با شناسه "{this_user_id}" در سیستم موجود نمی باشد.'
                    return JsonResponse(response_data)
            except Exception as e:
                response_data['status'] = '500'
                response_data['error'] = str(e)
                return JsonResponse(response_data)
        else:
            response_data['status'] = '403'
            response_data['error'] = 'شما اجازه دسترسی به این بخش را ندارید.'
            return JsonResponse(response_data)
    else:
        response_data['status'] = '401'
        response_data['error'] = 'شما وارد سیستم نشده اید.'
        return JsonResponse(response_data)


# deactive personal
def deactive_personal(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.is_governor:
            try:
                # get data
                this_user_id = request.POST.get('user_id')
                # check exists data
                if User.objects.filter(id = this_user_id).exists():
                    # get this user
                    this_user = User.objects.get(id = this_user_id)
                    # deactive object
                    this_user.active = False
                    this_user.save()

                    response_data['status'] = '200'
                    return JsonResponse(response_data)
                else:
                    # not exists data
                    response_data['status'] = '404'
                    response_data['error'] = 'کاربری با این شناسه موجود نیست.'
                    return JsonResponse(response_data)
            except Exception as e:
                response_data['status'] = '500'
                response_data['error'] = str(e)
                return JsonResponse(response_data)
        else:
            response_data['status'] = '403'
            response_data['error'] = 'شما اجازه دسترسی به این بخش را ندارید.'
            return JsonResponse(response_data)
    else:
        response_data['status'] = '401'
        response_data['error'] = 'شما وارد سیستم نشده اید.'
        return JsonResponse(response_data)


# active personal
def active_personal(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.is_governor:
            try:
                # get data
                this_user_id = request.POST.get('user_id')
                # check exists data
                if User.objects.filter(id = this_user_id).exists():
                    # get this user
                    this_user = User.objects.get(id = this_user_id)
                    # active object
                    this_user.active = True
                    this_user.save()

                    response_data['status'] = '200'
                    return JsonResponse(response_data)
                else:
                    # not exists data
                    response_data['status'] = '404'
                    response_data['error'] = 'کاربری با این شناسه موجود نیست.'
                    return JsonResponse(response_data)
            except Exception as e:
                response_data['status'] = '500'
                response_data['error'] = str(e)
                return JsonResponse(response_data)
        else:
            response_data['status'] = '403'
            response_data['error'] = 'شما اجازه دسترسی به این بخش را ندارید.'
            return JsonResponse(response_data)
    else:
        response_data['status'] = '401'
        response_data['error'] = 'شما وارد سیستم نشده اید.'
        return JsonResponse(response_data)