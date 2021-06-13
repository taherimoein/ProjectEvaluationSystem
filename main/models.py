from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.deconstruct import deconstructible
from django.db.models import JSONField
from django.utils import timezone
import random, string, datetime
from django.db import models

# ------------------------------------------------------------------------------------------------------------------------------------

@deconstructible
class default_history_field():
    def __call__(self):
        return {'list': []}


@deconstructible
class default_similar_projects_field():
    def __call__(self):
        return {'completed': 0, 'not_completed': 0}


@deconstructible
class default_requires_field():
    def __call__(self):
        return {'status': False, 'description': None}


@deconstructible
class create_validation_code():
    def __init__(self, size):
        self.size = size

    def __call__(self):
        code = ''.join(random.choice(string.digits) for i in range(self.size))
        return code

# --------------------------------------------------------------------------------------------------------------------------------------

# Validation (اعتبار سنجی) Model   
class Validation(models.Model):
    mobile = models.CharField(verbose_name = 'شماره موبایل', max_length = 11, unique = True)
    validation_code = models.CharField(verbose_name = 'کد فعال سازی', max_length = 6, default = create_validation_code(6))
    createdatetime = models.DateTimeField(verbose_name = 'تاریخ و زمان ایجاد', auto_now_add = True)

# --------------------------------------------------------------------------------------------------------------------------------------

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, father_s_name, birth_certificate_id, national_code, password, **kwargs):
        if not username:
            raise ValueError("Users must have username")
        if not first_name:
            raise ValueError("Users must have first name")
        if not last_name:
            raise ValueError("Users must have last name")
        if not father_s_name:
            raise ValueError("Users must have fathers name")
        if not birth_certificate_id:
            raise ValueError("Users must have birth certificate id")
        if not national_code:
            raise ValueError("Users must have national_code")
        if not password:
            raise ValueError("Users must have password")

        user = self.model(username = username, **kwargs)
        user.first_name = first_name
        user.last_name = last_name
        user.father_s_name = father_s_name
        user.birth_certificate_id = birth_certificate_id
        user.national_code = national_code
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, username, first_name, last_name, father_s_name, birth_certificate_id, national_code, password, **kwargs):
        user = self.model(username = username, staff = True, **kwargs)
        user.first_name = first_name
        user.last_name = last_name
        user.father_s_name = father_s_name
        user.birth_certificate_id = birth_certificate_id
        user.national_code = national_code
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, father_s_name, birth_certificate_id, national_code, password, **kwargs):
        user = self.model(username = username, staff = True, superuser = True, **kwargs)
        user.first_name = first_name
        user.last_name = last_name
        user.father_s_name = father_s_name
        user.birth_certificate_id = birth_certificate_id
        user.national_code = national_code
        user.set_password(password)
        user.save()
        return user

# --------------------------------------------------------------------------------------------------------------------------------------

# User (کاربر) Model
class User(AbstractBaseUser):
    # Personal Information
    first_name = models.CharField(verbose_name = 'first name', max_length = 50, db_index = True)
    last_name = models.CharField(verbose_name = 'last name', max_length = 150, db_index = True)
    father_s_name = models.CharField(verbose_name = 'fathers name', max_length = 50, db_index = True)
    GENDER_STATUS = (
        ('f', 'زن'),
        ('m', 'مزد')
    )
    gender = models.CharField(verbose_name = 'جنسیت', max_length = 1, choices = GENDER_STATUS, null = True)
    birth_certificate_id = models.CharField(verbose_name = 'birth certificate id', max_length = 10, unique = True, db_index = True)
    national_code = models.CharField(verbose_name = 'national code', max_length = 10, unique = True, db_index = True)
    birthday = models.DateField(verbose_name = 'تاریخ تولد', null = True)
    issue_place = models.CharField(verbose_name = 'issue place', max_length = 50)
    # Educational Information
    DEGREE_TYPE = (
        ('elementary', 'ابتدایی'),
        ('middle-school', 'سیکل'),
        ('diploma', 'دیپلم'),
        ('associate', 'فوق دیپلم'),
        ('bachelor', 'لیسانس'),
        ('master', 'فوق لیسانس'),
        ('phd', 'دکترا'),
        ('post-doctoral', 'فوق دکترا'),
    )
    degree = models.CharField(verbose_name = 'مقطع تحصیلی', max_length = 13, choices = DEGREE_TYPE, null = True)
    major = models.CharField(verbose_name = 'رشته تحصیلی', max_length = 255, null = True)
    university_of_study = models.CharField(verbose_name = 'دانشگاه محل تحصیل', max_length = 255, null = True)
    # Working information
    executive_device = models.CharField(verbose_name = 'دستگاه اجرایی', max_length = 255, null = True)
    role = models.CharField(verbose_name = 'سمت', max_length = 50, db_index = True, null = True)
    work_experience = models.TextField(verbose_name = 'سابقه کاری', null = True)
    personnel_id = models.CharField(verbose_name = 'شماره پرسنلی', max_length = 50, db_index = True, null = True)
    # Access information
    address = models.TextField(verbose_name = 'آدرس', null = True)
    zip_code = models.CharField(verbose_name = 'کدپستی', max_length = 10, null = True)
    mobile = models.CharField(verbose_name = 'شماره موبایل', max_length = 11, db_index = True, null = True)
    necessary_contact_number = models.CharField(verbose_name = 'شماره تماس ضروری', max_length = 11, null = True)
    workplace_number = models.CharField(verbose_name = 'شماره محل کار', max_length = 11, null = True)
    email = models.EmailField(verbose_name = 'ایمیل', null = True)
    # Profile information
    username = models.CharField(verbose_name = 'username', max_length = 50, db_index = True, unique = True)
    profile = models.ImageField(verbose_name = 'پروفایل', upload_to = 'media/images/user/profile/', default = 'static/images/default/default-profile.jpg')
    ACCESS_GROUP = (
        ('user','کاربر'),
        ('department_of_administration','ریاست اداره'),
        ('deputy_for_planning_and_civil_affairs','معاونت امور برنامه ریزی و عمرانی'),
        ('governor','فرماندار')
    )
    access_group = models.CharField(verbose_name = 'گروه دسترسی', max_length = 37, choices = ACCESS_GROUP, blank = True, null = True)
    # Attachments
    picture = models.ImageField(verbose_name = 'عکس', upload_to = 'media/images/user/picture/', blank = True, null = True)
    personal_id_card = models.ImageField(verbose_name = 'کارت شناسایی پرسنلی', upload_to = 'media/images/user/personal_id_card/', blank = True, null = True)
    device_introduction_letter = models.FileField(verbose_name = 'معرفی نامه دستگاه', upload_to = 'media/files/user/device_introduction_letter/', blank = True, null = True)
    sample_signature = models.ImageField(verbose_name = 'نمونه امضا', upload_to = 'media/images/user/signature/', blank = True, null = True)
    # Base information
    superuser = models.BooleanField(verbose_name = 'وضعیت مدیریت', default = False)
    staff = models.BooleanField(verbose_name = 'وضعیت کارمند', default = False)
    active = models.BooleanField(verbose_name = 'وضعیت فعالیت', default = True)
    history = JSONField(verbose_name = 'تاریخچه', default = default_history_field())
    create_date = models.DateTimeField(verbose_name = 'تاریخ ثبت کاربر', auto_now_add = True)
    update_date = models.DateTimeField(verbose_name = 'تاریخ بروزرسانی کاربر', auto_now = True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'father_s_name', 'birth_certificate_id', 'national_code']

    objects = UserManager()

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_governor(self):
        if self.access_group == 'governor':
            return True
        else:
            return False

    def get_access_group(self):
        try:
            group = {
                'user': 'کاربر',
                'department_of_administration': 'ریاست اداره',
                'deputy_for_planning_and_civil_affairs': 'معاونت امور برنامه ریزی و عمرانی',
                'governor': 'فرماندار'
            }
            return group[self.access_group]
        except:
            return None

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.national_code)

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_fullname(self):
        return ' '.join([self.first_name, self.last_name])

    def add_history(self, status, user = None, other_fileds = None, add_datetime = None,):
        if add_datetime is None:
            add_datetime = timezone.localtime(datetime.datetime.now())
        if user is not None:
            user = int(user)
        if status == 'create':
            self.history = {'list': [{'status': status, 'user': user, 'datetime': add_datetime.strftime("%Y-%m-%d %H:%M")}]}
        elif status == 'edit':
            self.history['list'].append({'status': status, 'user': user, 'datetime': add_datetime.strftime("%Y-%m-%d %H:%M"), 'fields' : other_fileds})
        elif status == 'confirmation':
            self.history['list'].append({'status': status, 'user': user, 'datetime': add_datetime.strftime("%Y-%m-%d %H:%M"), 'fields' : other_fileds})
        self.save()

    class Meta:
        ordering = ('id', 'create_date',)
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

# --------------------------------------------------------------------------------------------------------------------------------------

# Project (پروژه) Model
class Project(models.Model):
    title = models.CharField(verbose_name = 'عنوان', max_length = 255, db_index = True)
    description = models.TextField(verbose_name = 'توضیحات پروژه')
    fiscal_year = models.CharField(verbose_name = 'سال مالی', max_length = 4)
    executive_device = models.CharField(verbose_name = 'دستگاه اجرایی', max_length = 255, null = True)
    fk_user = models.ForeignKey(User, verbose_name = 'کاربر ثبت کننده', related_name = 'project_user', on_delete = models.SET_NULL, null = True)
    attached_file = models.FileField(verbose_name = 'فایل پیوست', upload_to = 'media/files/project/', blank = True, null = True)
    project_location_address = models.TextField(verbose_name = 'آدرس محل پروژه')
    telephone = models.CharField(verbose_name = 'شماره تماس', max_length = 8)
    approximate_date_preparation = models.DateField(verbose_name = 'تاریخ تقریبی بهره برداری')
    amount_required_for_workshop = models.CharField(verbose_name = 'مبلغ مورد نیاز برای تجهیز کارگاه', max_length = 15)
    prepayment_amount = models.CharField(verbose_name = 'مبلغ پیش پرداخت', max_length = 15)
    initial_offered_credit_amount = models.CharField(verbose_name = 'مبلغ اعتبار پیشنهاد اولیه', max_length = 15)
    amount_credit_increase = models.CharField(verbose_name = 'میزان مبلغ افزایش اعتبار', max_length = 15)
    bidding_history = models.BooleanField(verbose_name = 'سابقه انجام مناقصه', default = False)
    land_and_basic_facilities = models.BooleanField(verbose_name = 'زمین و امکانات اولیه', default = False)
    similar_projects = JSONField(verbose_name = 'پروژه های مشابه', default = default_similar_projects_field())
    ability_to_shred = models.BooleanField(verbose_name = 'قابلیت کوچک شدن', default = False)
    type_of_financial_resources = models.TextField(verbose_name = 'نوع منابع مالی')
    applicant_name_and_role = models.CharField(verbose_name = 'نام درخواست کننده / سمت', max_length = 255)
    requires_collaboration_between_devices = JSONField(verbose_name = 'نیاز به همکاری بین دستگاه', default = default_requires_field())
    requires_special_permissions = JSONField(verbose_name = 'نیاز مجوز خاص', default = default_requires_field())
    requires_special_facilities = JSONField(verbose_name = 'نیاز امکانات خاص', default = default_requires_field())
    shared_capability_between_multiple_executive_devices = JSONField(verbose_name = 'قابلیت اشتراکی بین چند دستگاه اجرایی', default = default_requires_field())
    shared_capability_between_several_cities = JSONField(verbose_name = 'قابلیت اشتراکی بین چند شهرستان', default = default_requires_field())
    history = JSONField(verbose_name = 'تاریخچه', default = default_history_field())
    create_date = models.DateTimeField(verbose_name = 'تاریخ ثبت', auto_now_add = True)
    update_date = models.DateTimeField(verbose_name = 'تاریخ بروزرسانی', auto_now = True)

    def __str__(self):
       return "{}".format(self.title)

    def add_history(self, status, user, other_fileds = None, add_datetime = None,):
        if add_datetime is None:
            add_datetime = timezone.localtime(datetime.datetime.now())
        user = int(user)

        if status == 'create':
            self.history = {'list': [{'status': status, 'user': user, 'datetime': add_datetime.strftime("%Y-%m-%d %H:%M")}]}
        elif status == 'edit':
            self.history['list'].append({'status': status, 'user': user, 'datetime': add_datetime.strftime("%Y-%m-%d %H:%M"), 'fields' : other_fileds})
        self.save()

    class Meta:
        ordering = ('id', 'create_date')   
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"

#----------------------------------------------------------------------------------------------------------------------------------------