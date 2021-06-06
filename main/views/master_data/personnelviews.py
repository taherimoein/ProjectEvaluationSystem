from main.serializers.master_data import UserBaseSerializer
# , ManagementBaseSerializer, JobTitleBaseSerializer, \
#     UserSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, get_object_or_404
from utils.decorators.access_level import is_governor
from utils.base_fuction import is_valid_national_code
# from main.serializers import PersonnelSerializer
# from utils.base_fuction import convert_to_regex
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

    context = {

    }
    return render(request, 'master-data/personnel/personnel-create.html', context)


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


def get_user_details(this_user):
    this_user_details = {
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
    return render(request, 'master-data/personnel/personnel-edit.html', context)


def confirmation_of_information_personnel(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.is_governor:
            try:
                # get data
                this_user_id = request.POST.get('id')
                this_access_group = request.POST.get('access_group')

                if User.objects.filter(id = this_user_id).exists():
                    if (this_access_group == 'user') or (this_access_group == 'department_of_administration'):
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