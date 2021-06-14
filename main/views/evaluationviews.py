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
        'ProjectType_list': project_type_list
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
                response_data['error'] = 'پروژه ای با این شناسه که متعلق به شما باشد، در سیستم موجوئ نمی باشد.'
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


@is_governor
@login_required(login_url = 'main:sign_page')
def evaluation_gov_page(request, project_id):
    this_project = get_object_or_404(Project, id = project_id)

    context = {
        'ThisProject': this_project
    }

    return render(request, 'main/evaluation/evaluation-gov-page.html', context)

@is_deputy
@login_required(login_url = 'main:sign_page')
def evaluation_assistant_page(request, project_id):
    this_project = get_object_or_404(Project, id = project_id)

    context = {
        'ThisProject': this_project
    }

    return render(request, 'main/evaluation/evaluation-assistant-page.html', context)