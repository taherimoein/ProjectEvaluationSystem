
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
def organization_list_page(request):
#     users = User.objects.annotate(fullname = Concat('first_name', Value(' '), 'last_name')) \
#         .order_by('create_date').values('id', 'national_code', 'fullname', 'father_s_name', \
#             'role', 'executive_device', 'personnel_id', 'necessary_contact_number',\
#             'mobile', 'username', 'access_group', 'active')

#     context = {
#         'Users': users
#     }
    return render(request, 'master-data/organization/organization-list.html', )


@is_governor
@login_required(login_url = 'main:sign_page')
def organization_create_page(request):
    return render(request, 'master-data/organization/organization-create.html', )
