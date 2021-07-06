
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, get_object_or_404
from utils.decorators.access_level import is_governor
from utils.base_fuction import is_valid_national_code
from django.utils import timezone
# from main.serializers import PersonnelSerializer
# from utils.base_fuction import convert_to_regex
from django.db.models.functions import Concat
from django.db.models import Value, Q
from django.http import JsonResponse
import json
# get model
from main.models import ProjectType, User

# -------------------------------------------------------------------------------------------------------------------------------------

@is_governor
@login_required(login_url = 'main:sign_page')
def projectstype_list_page(request):
    projectstype_list = ProjectType.objects.all().values('id', 'title', 'score', 'create_date')
    context = {
        'projectstype': projectstype_list
    }
    return render(request, 'master-data/projectstype/projectstype-list.html', context )


@is_governor
@login_required(login_url = 'main:sign_page')
def projectstype_create_page(request):
    return render(request, 'master-data/projectstype/projectstype-create.html', )

     
# create new project_type
def create_new_project_type(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.access_group == 'governor' :
            try:
                # get data
                title = request.POST.get('title')
                score = request.POST.get('score')
                # check data
                if (len(title) > 0) and ((len(score) > 0)):
                    # check duplicate data
                    if not ProjectType.objects.filter(title = title, score = score).exists():
                        # create new object
                        this_project_type = ProjectType.objects.create(title = title, score = score)
                        # add create history
                        # this_project_type.add_history('create', request.user.id, timezone.now())

                        response_data['status'] = '201'
                        return JsonResponse(response_data)
                    else:
                        # duplicate data
                        response_data['status'] = '406'
                        response_data['error'] = 'نوع پروژه ای با این مشخصات قبلا ثبت شده است.'
                        return JsonResponse(response_data)
                else:
                    response_data['status'] = '400'
                    response_data['error'] = 'شرح و امتیاز اجباری می باشد.'
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
 

# delete ProjectType
def delete_project_type(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.access_group == 'governor' :
            try:
                # get data
                this_project_type_id = request.POST.get('project_type_id')
                # check exists data
                if ProjectType.objects.filter(id = this_project_type_id).exists():
                    # get this project_type
                    this_project_type = ProjectType.objects.get(id = this_project_type_id)
                    # delete object
                    this_project_type.delete()

                    response_data['status'] = '200'
                    return JsonResponse(response_data)
                else:
                    # not exists data
                    response_data['status'] = '404'
                    response_data['error'] = 'نوع پروژه ای با این شناسه موجود نیست.'
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