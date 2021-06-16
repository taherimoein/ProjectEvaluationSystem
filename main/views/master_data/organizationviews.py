from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, get_object_or_404
from utils.decorators.access_level import is_governor
from django.db.models.functions import Concat
from django.db.models import Value, Q
from django.http import JsonResponse
import json
# get model
from main.models import User, Executive_Device

# -------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url = 'main:sign_page')
def organization_list_page(request):
    #     users = User.objects.annotate(fullname = Concat('first_name', Value(' '), 'last_name')) \
    #         .order_by('create_date').values('id', 'national_code', 'fullname', 'father_s_name', \
    #             'role', 'executive_device', 'personnel_id', 'necessary_contact_number',\
    #             'mobile', 'username', 'access_group', 'active')

    #     context = {
    #         'Users': users
    #     }
    return render(request, 'master-data/organization/organization-list.html', )


@login_required(login_url = 'main:sign_page')
def organization_create_page(request):
    return render(request, 'master-data/organization/organization-create.html', )


def create_organization(request):
    response_data = {}
    if request.user.is_authenticated:
        try:
            # get data
            this_code = request.POST.get('code')
            this_title = request.POST.get('title')
            this_year = request.POST.get('year')
            this_address_general_administration = request.POST.get('address_general_administration')
            this_telephone = request.POST.get('telephone')
            this_fax = request.POST.get('fax')
            this_email = request.POST.get('email')
            this_website = request.POST.get('website')
            this_boss_executive_device = json.loads(request.POST.get('boss_executive_device'))
            this_assistance_executive_device = json.loads(request.POST.get('assistance_executive_device'))
            this_number_employees = request.POST.get('number_employees')
            this_number_contract_staff = request.POST.get('number_contract_staff')
            this_number_buildings = request.POST.get('number_buildings')
            this_number_unreinforced_buildings = request.POST.get('number_unreinforced_buildings')
            this_buildings = json.loads(request.POST.get('buildings'))
            this_projects_behind_schedule = json.loads(request.POST.get('projects_behind_schedule'))
            this_projects_not_been_completed_more_year = request.POST.get('projects_not_been_completed_more_year')
            this_number_projects_last_year = request.POST.get('number_projects_last_year')
            this_number_completed_financial_projects = request.POST.get('number_completed_financial_projects')
            this_amount_budget_requested_last_year = request.POST.get('amount_budget_requested_last_year')
            this_budget_realized_last_year = request.POST.get('budget_realized_last_year')
            this_amount_budget_allocated_last_year = request.POST.get('amount_budget_allocated_last_year')
            this_number_completed_projects = request.POST.get('number_completed_projects')
            this_number_projects_remaining = request.POST.get('number_projects_remaining')
            this_number_projects_is_behind_schedule = request.POST.get('number_projects_is_behind_schedule')
            this_number_projects_not_been_completed_more_year = request.POST.get('number_projects_not_been_completed_more_year')
            # create organization
            this_organization = Executive_Device.objects.create(code = this_code, title = this_title, year = this_year,\
                executive_device = this_executive_device, telephone = this_telephone, fax = this_fax, email = this_email,\
                address_general_administration = this_address_general_administration, approximate_date_preparation = this_approximate_date_preparation,\
                website = this_website, boss_executive_device = this_boss_executive_device, assistance_executive_device = this_assistance_executive_device,\
                number_employees = this_number_employees, number_contract_staff = this_number_contract_staff, number_buildings = this_number_buildings,\
                number_unreinforced_buildings = this_number_unreinforced_buildings, buildings = this_buildings, projects_behind_schedule = this_projects_behind_schedule,\
                projects_not_been_completed_more_year = this_projects_not_been_completed_more_year, number_projects_last_year = this_number_projects_last_year,\
                number_completed_financial_projects = this_number_completed_financial_projects, amount_budget_requested_last_year = this_amount_budget_requested_last_year,\
                budget_realized_last_year = this_budget_realized_last_year, amount_budget_allocated_last_year = this_amount_budget_allocated_last_year,\
                number_completed_projects = this_number_completed_projects, number_projects_remaining = this_number_projects_remaining,\
                number_projects_is_behind_schedule = this_number_projects_is_behind_schedule,\
                number_projects_not_been_completed_more_year = this_number_projects_not_been_completed_more_year)

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


@is_governor
@login_required(login_url = 'main:sign_page')
def evaluation_governor_page(request, organization_id):
    this_organization = get_object_or_404(Executive_Device, id = organization_id)

    context = {
        'ThisExecutiveDevice': this_organization
    }

    return render(request, 'main/evaluation/evaluation-gov-page.html', context)


def executive_device_evaluation_governor(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.user.is_governor:
            try:
                # get data
                this_organization_id = request.POST.get('organization_id')
                if not Executive_Device.objects.filter(id = this_organization_id).exists():
                    response_data['status'] = '404'
                    response_data['error'] = 'دستگاه اجرایی با این شناسه در سیستم موجود نمی باشد.'
                    return JsonResponse(response_data)
                else:
                    this_assessment = request.POST.get('assessment')
                # add evaluation executive_device info
                this_organization = Executive_Device.objects.get(id = this_organization_id)
                # get point from assessment
                this_organization.evaluation_governor = int(this_assessment)
                this_organization.evaluation_point += int(this_assessment)
                this_organization.save()
                
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