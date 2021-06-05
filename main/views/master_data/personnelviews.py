# from main.serializer.master_data import UserBaseSerializer, ManagementBaseSerializer, JobTitleBaseSerializer, \
#     UserSerializer
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import  render, get_object_or_404
# # from main.serializers import PersonnelSerializer
# # from utils.base_fuction import convert_to_regex
# from django.db.models.functions import Concat
# from django.db.models import Value, Q
# from django.http import JsonResponse
# import json
# # get model
# from main.models import User, Deputy, Management, JobGroup, JobTitle, Company, WorkStation

# # # -------------------------------------------------------------------------------------------------------------------------------------

# @login_required(login_url = 'main:sign_page')
# def personnel_list_page(request):
#     users = User.objects.annotate(fullname = Concat('first_name', Value(' '), 'last_name')) \
#         .order_by('created_date').values('id', 'national_code', 'fullname', 'father_s_name', \
#             'organization_role', 'job_title__fk_jobgroup__title', 'job_title__title', \
#             'management__fk_deputy__title', 'management__title', 'mobile', 'active')

#     companies = Company.objects.order_by('created_date').values('id', 'title')

#     deputies = Deputy.objects.filter(publish = True).order_by('created_date').values('id', 'title')
#     managements = Management.objects.filter(publish = True)
#     managements = ManagementBaseSerializer(managements, many = True)

#     job_groups = JobGroup.objects.filter(publish = True).order_by('created_date').values('id', 'title')
#     job_titles = JobTitle.objects.filter(publish = True)
#     job_titles = JobTitleBaseSerializer(job_titles, many = True)

#     context = {
#         'Users': users,
#         'Companies': companies,
#         'Deputies': deputies,
#         'Managements': json.dumps(managements.data),
#         'JobGroups': job_groups,
#         'JobTitles': json.dumps(job_titles.data),
#     }
#     return render(request, 'master-data/personnel/personnel-list.html', context)


# @login_required(login_url = 'main:sign_page')
# def personnel_create_page(request):
#     deputies = Deputy.objects.filter(publish = True).values('id', 'title')
#     managements = Management.objects.filter(publish = True)
#     managements = ManagementBaseSerializer(managements, many = True)

#     job_groups = JobGroup.objects.filter(publish = True).values('id', 'title')
#     job_titles = JobTitle.objects.filter(publish = True)
#     job_titles = JobTitleBaseSerializer(job_titles, many = True)

#     context = {
#         'Deputies': deputies,
#         'Managements': json.dumps(managements.data),
#         'JobGroups': job_groups,
#         'JobTitles': json.dumps(job_titles.data)
#     }
#     return render(request, 'master-data/personnel/personnel-create.html', context)
    

# # @login_required(login_url = 'main:sign_page')
# # def personnel_edit_page(request, this_national_code):
# #     this_user = get_object_or_404(User, national_code = this_national_code)

# #     deputies = Deputy.objects.order_by('created_date').values('id', 'title')
# #     managements = Management.objects.all()
# #     managements = ManagementSerializer(managements, many = True)

# #     job_groups = JobGroup.objects.order_by('created_date').values('id', 'title')
# #     job_titles = JobTitle.objects.all()
# #     job_titles = JobTitleSerializer(job_titles, many = True)

# #     workstations = WorkStation.objects.order_by('created_date').values('id', 'title')
# #     sections = Section.objects.all()
# #     sections = SectionBaseSerializer(sections, many = True)

# #     context = {
# #         'ThisUser': get_user_details(this_user),
# #         'Deputies': deputies,
# #         'Managements': json.dumps(managements.data),
# #         'JobGroups': job_groups,
# #         'JobTitles': json.dumps(job_titles.data),
# #         'WorkStations': workstations,
# #         'Sections': json.dumps(sections.data),
# #     }
# #     return render(request, 'master-data/personnel/personnel-edit.html', context)


# # def get_user_details(this_user):
# #     this_user_details = {
# #         'national_code': this_user.national_code,
# #         'first_name': this_user.first_name,
# #         'last_name': this_user.last_name,
# #         'profile': this_user.profile,
# #         'father_s_name': this_user.father_s_name,
# #         'birth_certificate_id': this_user.birth_certificate_id,
# #         'birthday': this_user.birthday,
# #         'birthplace': this_user.birthplace,
# #         'gender': this_user.gender,
# #         'marital_status': this_user.marital_status,
# #         'number_of_children': this_user.number_of_children,
# #         'degree': this_user.degree,
# #         'telephone': this_user.telephone,
# #         'mobile': this_user.mobile,
# #         'address': this_user.address,
# #         'insurance_number': this_user.insurance_number,
# #         'organization_role': this_user.organization_role,
# #         'job_title': json.dumps(JobTitleSerializer(this_user.job_title).data),
# #         'management': json.dumps(ManagementSerializer(this_user.management).data),
# #         'sections': this_user.get_sections()
# #     }
# #     return this_user_details


# # @login_required(login_url = 'main:sign_page')
# # def personnel_details_page(request, this_national_code):
# #     this_user = get_object_or_404(User, national_code = this_national_code)

# #     context = {
# #         'ThisUser': get_user_details(this_user)
# #     }
# #     return render(request, 'master-data/personnel/personnel-details.html', context)


# def search_in_users(request):
#     response_data = {}
#     try:
#         # get search
#         this_search = request.POST.get('search')
#         # set search regex
#         this_search = this_search.split(' ')
#         this_search = list(filter(lambda i: i != '', this_search))
#         search_word_list = []
#         for word in this_search:
#             search_word = list(map(lambda x: x + '\s*', word.replace(' ','')[:-1]))
#             search_word = ''.join(search_word) + word[-1]
#             search_word_list.append(search_word)
#         search_word = r'.*'.join(search_word_list)
#         # search in fullname & national_code
#         users = User.objects.annotate(full_name = Concat('first_name', Value(' '), 'last_name')).filter(Q(full_name__regex = search_word) | Q(national_code__regex = search_word))
#         serializer = UserBaseSerializer(users, many = True)

#         response_data['status'] = '200'
#         response_data['data'] = serializer.data
#         return JsonResponse(response_data)
#     except Exception as e:
#         response_data['status'] = '500'
#         response_data['error'] = str(e)
#         return JsonResponse(response_data)


# # class PersonnelCreate(generics.CreateAPIView):
    
# #     serializer_class = PersonnelSerializer
# #     permission_classes = (AllowAny,)


# # class PersonnelRetrieveUpdate(generics.RetrieveUpdateAPIView):

# #     serializer_class = PersonnelSerializer
# #     permission_classes = (AllowAny,)

# #     def get_queryset(self):
# #         personnel = User.objects.filter(id=self.kwargs['pk'])
# #         return personnel


# # def create_personnel(request):
# #     response_data = {}
# #     if request.user.is_authenticated:
# #         try:
# #             # get data
# #             this_content = request.POST.get('content')
# #             # try:
# #             #     this_user_profile = request.FILES['profile']
# #             # except:
# #             #     this_user_profile = None
# #             # check fields
# #             check_fields_status, error, this_user_company = check_personnel_fields(this_user_first_name, this_user_last_name, this_user_national_code, this_user_mobile, this_user_role, this_user_company, this_user_access_group, this_user_relevant_deputy, this_user_relevant_unit, this_user_active)
# #             if check_fields_status:
# #                 # create new object 
# #                 this_user = User.objects.create_user(this_user_national_code, this_user_national_code)
# #                 # add other field to user
# #                 this_user.first_name = this_user_first_name
# #                 this_user.last_name = this_user_last_name
# #                 this_user.role = this_user_role
# #                 this_user.company = this_user_company
# #                 this_user.mobile = this_user_mobile
# #                 this_user.access_group = this_user_access_group
# #                 this_user.relevant_deputy = int(this_user_relevant_deputy)
# #                 this_user.relevant_unit = int(this_user_relevant_unit)
# #                 this_user.active = this_user_active
# #                 if this_user_email is not None:
# #                     if not re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', this_user_email):
# #                         response_data['status'] = '400'
# #                         response_data['error'] = 'ایمیل وارد شده معتبر نمی باشد.'
# #                         return JsonResponse(response_data)
# #                     else:
# #                         this_user.email = this_user_email
# #                 if this_user_local_telephone is not None:
# #                     if not re.search(r'^[1-9]\d{0,1}\d{0,6}$', this_user_local_telephone):
# #                         response_data['status'] = '400'
# #                         response_data['error'] = 'شماره تلفن ثابت وارد شده معتبر نمی باشد.'
# #                         return JsonResponse(response_data)
# #                     else:
# #                         this_user.local_telephone = this_user_local_telephone
# #                 if this_user_profile is not None:
# #                     this_user.profile = this_user_profile
# #                 this_user.save()

# #                 # add create history
# #                 this_user.add_history('create', request.user.id, timezone.now())

# #                 response_data['status'] = '201'
# #                 return JsonResponse(response_data)
# #             else:
# #                 response_data['status'] = '400'
# #                 response_data['error'] = error
# #                 return JsonResponse(response_data)
# #         except Exception as e:
# #             response_data['status'] = '500'
# #             response_data['error'] = str(e)
# #             return JsonResponse(response_data)
# #     else:
# #         response_data['status'] = '401'
# #         response_data['error'] = 'شما وارد سیستم نشده اید.'
# #         return JsonResponse(response_data)