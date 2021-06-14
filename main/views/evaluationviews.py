from utils.decorators.access_level import is_governor, is_deputy
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from utils.base_fuction import is_valid_national_code
from django.db.models.functions import Concat
from django.db.models import Value, Q
from django.http import JsonResponse
from django.conf import settings
import json
# get model
from main.models import User, Project, ProjectType

# -------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url = 'main:sign_page')
def evaluation_user_page(request, project_id):
    this_project = get_object_or_404(Project, id = project_id)
    project_type_list = ProjectType.objects.all()

    context = {
        'ThisProject': this_project,
        'ProjectTypeList': project_type_list
    }

    return render(request, 'main/evaluation/evaluation-user-page.html', context)


def project_evaluation_user(request):
    response_data = {}
    if request.user.is_authenticated:
        try:
            # get data
            this_project_id = request.POST.get('project_id')
            if not Project.objects.filter(id = this_project_id, fk_user = request.user).exists():
                response_data['status'] = '404'
                response_data['error'] = 'پروژه ای با این شناسه که متعلق به شما باشد، در سیستم موجود نمی باشد.'
                return JsonResponse(response_data)
            else:
                this_assessment = json.loads(request.POST.get('assessment'))
                try:
                    this_rationale_studies_file = request.FILES['rationale_studies_file']
                except:
                    this_rationale_studies_file = None
            # add evaluation project info
            this_project = Project.objects.get(id = this_project_id)
            # upload files
            file_url = None
            if this_rationale_studies_file is not None:
                file_storage = FileSystemStorage(location = settings.MEDIA_ROOT + '/media/files/evaluation', base_url = '/media/files/evaluation')
                data = file_storage.save(this_rationale_studies_file.name, this_rationale_studies_file)
                file_url = file_storage.url(data)
            this_assessment['rationale_studies']['file'] = file_url
            # get point from assessment
            sum_point = 0
            sum_point += this_assessment['rationale_studies']['point']
            sum_point += this_assessment['comprehensive_target_needs']['point']
            sum_point += this_assessment['comprehensive_necessity_of_purpose']['point']
            sum_point += this_assessment['project_implementation_time']['point']
            sum_point += this_assessment['repetition_rate']['point']
            sum_point += this_assessment['abundance_rate']['point']
            sum_point += this_assessment['population']['point']
            sum_point += this_assessment['type_of_project']['point']

            this_project.evaluation_user = this_assessment
            this_project.evaluation_point += sum_point
            this_project.save()

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


@is_deputy
@login_required(login_url = 'main:sign_page')
def evaluation_assistant_page(request, project_id):
    this_project = get_object_or_404(Project, id = project_id)

    context = {
        'ThisProject': this_project
    }

    return render(request, 'main/evaluation/evaluation-assistant-page.html', context)


def project_evaluation_assistant(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.is_deputy:
            try:
                # get data
                this_project_id = request.POST.get('project_id')
                if not Project.objects.filter(id = this_project_id).exists():
                    response_data['status'] = '404'
                    response_data['error'] = 'پروژه ای با این شناسه در سیستم موجود نمی باشد.'
                    return JsonResponse(response_data)
                else:
                    this_assessment = json.loads(request.POST.get('assessment'))
                # add evaluation project info
                this_project = Project.objects.get(id = this_project_id)
                # get point from assessment
                sum_point = 0
                sum_point += this_assessment['importance_of_project']['point']
                sum_point += this_assessment['expert_opinion']['point']

                this_project.evaluation_assistance = this_assessment
                this_project.evaluation_point += sum_point
                this_project.save()
                # Calculate z
                total_amount_of_city_s_annual_budget = this_assessment['total_amount_of_city_s_annual_budget']
                # دریافت کل مبالغ پیشنهادی دستگاه اجرایی
                executive_device_total_price = 0
                for item in Project.objects.filter(executive_device = this_project.executive_device):
                    executive_device_total_price += int(item.initial_offered_credit_amount)
                z = total_amount_of_city_s_annual_budget / 42
                # Calculate Z score
                if executive_device_total_price <= z:
                    z_point = 100
                elif executive_device_total_price <= (2 * z):
                    z_point = 75
                elif executive_device_total_price <= (3 * z):
                    z_point = 50
                else:
                    z_point = 20
                # save z info
                z_info = {'total_amount_of_city_s_annual_budget': total_amount_of_city_s_annual_budget,\
                    'executive_device_total_price': executive_device_total_price, 'z': z, 'z_point': z_point}
                this_project.equal_distribution_credits_between_executive_devices = z_info
                this_project.evaluation_point += z_point
                this_project.save()
                
                response_data['status'] = '200'
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


@is_governor
@login_required(login_url = 'main:sign_page')
def evaluation_governor_page(request, project_id):
    this_project = get_object_or_404(Project, id = project_id)

    context = {
        'ThisProject': this_project
    }

    return render(request, 'main/evaluation/evaluation-gov-page.html', context)


def project_evaluation_governor(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.is_governor:
            try:
                # get data
                this_project_id = request.POST.get('project_id')
                if not Project.objects.filter(id = this_project_id).exists():
                    response_data['status'] = '404'
                    response_data['error'] = 'پروژه ای با این شناسه در سیستم موجود نمی باشد.'
                    return JsonResponse(response_data)
                else:
                    this_assessment = json.loads(request.POST.get('assessment'))
                # add evaluation project info
                this_project = Project.objects.get(id = this_project_id)
                # get point from assessment
                sum_point = 0
                sum_point += this_assessment['role_ecutive_device_management']['point']

                this_project.evaluation_governor = this_assessment
                this_project.evaluation_point += sum_point
                this_project.save()
                
                response_data['status'] = '200'
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