from utils.decorators.access_level import is_governor, is_governor_or_deputy
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, get_object_or_404
from django.db.models.functions import Concat
from django.db.models import Value, Q
from django.http import JsonResponse
import json
# get model
from main.models import User, Project, Executive_Device

# -------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url = 'main:sign_page')
def project_list_page(request):
    project_list = Project.objects.filter(fk_user = request.user).order_by('-create_date')\
        .values('id', 'title', 'create_date')

    context = {
        'ProjectList': project_list
    }
    return render(request, 'master-data/project/project-list.html', context)


@is_governor_or_deputy
@login_required(login_url = 'main:sign_page')
def project_list_all_page(request):
    project_list = Project.objects.order_by('-create_date')\
        .values('id', 'title', 'create_date')

    context = {
        'ProjectList': project_list
    }
    return render(request, 'master-data/project/project-list-all.html', context)


@login_required(login_url = 'main:sign_page')
def project_create_page(request):
    return render(request, 'master-data/project/project-create.html')


def create_project(request):
    response_data = {}
    if request.user.is_authenticated:
        try:
            # get data
            this_title = request.POST.get('title')
            this_description = request.POST.get('description')
            this_fiscal_year = request.POST.get('fiscal_year')
            this_executive_device = request.POST.get('executive_device')
            this_project_location_address = request.POST.get('project_location_address')
            this_telephone = request.POST.get('telephone')
            this_approximate_date_preparation = request.POST.get('approximate_date_preparation')
            this_amount_required_for_workshop = request.POST.get('amount_required_for_workshop')
            this_prepayment_amount = request.POST.get('prepayment_amount')
            this_initial_offered_credit_amount = request.POST.get('initial_offered_credit_amount')
            this_amount_credit_increase = request.POST.get('amount_credit_increase')
            this_bidding_history = json.loads(request.POST.get('bidding_history'))
            this_land_and_basic_facilities = json.loads(request.POST.get('land_and_basic_facilities'))
            this_similar_projects = json.loads(request.POST.get('similar_projects'))
            this_ability_to_shred = json.loads(request.POST.get('ability_to_shred'))
            this_type_of_financial_resources = request.POST.get('type_of_financial_resources')
            this_applicant_name_and_role = request.POST.get('applicant_name_and_role')
            this_requires_collaboration_between_devices = json.loads(request.POST.get('requires_collaboration_between_devices'))
            this_requires_special_permissions = json.loads(request.POST.get('requires_special_permissions'))
            this_requires_special_facilities = json.loads(request.POST.get('requires_special_facilities'))
            this_shared_capability_between_multiple_executive_devices = json.loads(request.POST.get('shared_capability_between_multiple_executive_devices'))
            this_shared_capability_between_several_cities = json.loads(request.POST.get('shared_capability_between_several_cities'))
            try:
                this_attached_file = request.FILES['attached_file']
            except:
                this_attached_file = None
            # create project
            this_project = Project.objects.create(title = this_title, description = this_description, fiscal_year = this_fiscal_year,\
                executive_device = this_executive_device, fk_user = request.user, project_location_address = this_project_location_address,\
                telephone = this_telephone, approximate_date_preparation = this_approximate_date_preparation,\
                amount_required_for_workshop = this_amount_required_for_workshop, prepayment_amount = this_prepayment_amount,\
                initial_offered_credit_amount = this_initial_offered_credit_amount, amount_credit_increase = this_amount_credit_increase,\
                type_of_financial_resources = this_type_of_financial_resources, applicant_name_and_role = this_applicant_name_and_role)
            # check other fields
            if this_attached_file is not None:
                this_project.attached_file = this_attached_file
            if this_bidding_history:
                this_project.bidding_history = True
            if this_land_and_basic_facilities:
                this_project.land_and_basic_facilities = True
            if (this_similar_projects['completed'] > 0) or (this_similar_projects['not_completed'] > 0):
                this_project.similar_projects = this_similar_projects
            if this_ability_to_shred:
                this_project.ability_to_shred = True
            if this_requires_collaboration_between_devices['status']:
                this_project.requires_collaboration_between_devices = this_requires_collaboration_between_devices
            if this_requires_special_permissions['status']:
                this_project.requires_special_permissions = this_requires_special_permissions
            if this_requires_special_facilities['status']:
                this_project.requires_special_facilities = this_requires_special_facilities
            if this_shared_capability_between_multiple_executive_devices['status']:
                this_project.shared_capability_between_multiple_executive_devices = this_shared_capability_between_multiple_executive_devices
            if this_shared_capability_between_several_cities['status']:
                this_project.shared_capability_between_several_cities = this_shared_capability_between_several_cities
            this_project.save()

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


def get_project_details(this_project):
    this_executive_device = Executive_Device.objects.get(title = this_project.executive_device)

    this_project_details = {
        'title': this_project.title,
        'description': this_project.description,
        'fiscal_year': this_project.fiscal_year,
        'executive_device': this_project.executive_device,
        'fk_user': this_project.fk_user,
        'attached_file': this_project.attached_file,
        'project_location_address': this_project.project_location_address,
        'telephone': this_project.telephone,
        'approximate_date_preparation': this_project.approximate_date_preparation,
        'amount_required_for_workshop': this_project.amount_required_for_workshop,
        'prepayment_amount': this_project.prepayment_amount,
        'initial_offered_credit_amount': this_project.initial_offered_credit_amount,
        'amount_credit_increase': this_project.amount_credit_increase,
        'bidding_history': this_project.bidding_history,
        'land_and_basic_facilities': this_project.land_and_basic_facilities,
        'similar_projects': this_project.similar_projects,
        'ability_to_shred': this_project.ability_to_shred,
        'type_of_financial_resources': this_project.type_of_financial_resources,
        'applicant_name_and_role': this_project.applicant_name_and_role,
        'requires_collaboration_between_devices': this_project.requires_collaboration_between_devices,
        'requires_special_permissions': this_project.requires_special_permissions,
        'requires_special_facilities': this_project.requires_special_facilities,
        'shared_capability_between_multiple_executive_devices': this_project.shared_capability_between_multiple_executive_devices,
        'shared_capability_between_several_cities': this_project.shared_capability_between_several_cities,
        'evaluation_assistance': this_project.evaluation_assistance,
        'evaluation_user': this_project.evaluation_user,
        'executive_device_point': this_executive_device.evaluation_governor,
        'equal_distribution_credits_between_executive_devices': this_project.equal_distribution_credits_between_executive_devices,
        'evaluation_point': this_project.evaluation_point,
        'create_date': this_project.evaluation_point
    }
    return this_project_details


@login_required(login_url = 'main:sign_page')
def project_details_page(request, pk):
    this_project = get_object_or_404(Project, id = pk)

    context = {
        'ThisProject': get_project_details(this_project)
    }
    return render(request, 'master-data/project/project-details.html', context)