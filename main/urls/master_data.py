from main.views.master_data import personnelviews
from django.urls import path

# -----------------------------------------------------------------------------------------------------------------------------------

app_name = 'master_data'
urlpatterns = [
    # Master Data "company" -------------------------------------------------------------
    # path('company/', companyviews.company_list_page, name = 'company_list_page'),
    # path('company/create/', companyviews.company_create_page, name = 'company_create_page'),
    # path('ajax/company/create/', companyviews.create_company, name = 'ajax_company_create'),
#     path('company/edit/<str:this_code>/', companyviews.company_edit_page, name='company_edit_page'),
#     path('api/company/edit/<int:pk>/', companyviews.CompanyRetrieveUpdate.as_view(), name='api_company_edit'),
    # path('ajax/company/search/', companyviews.search_in_companies, name = 'ajax_search_in_companies'),
    # Master Data "deputy" --------------------------------------------------------------
    # path('deputy/', deputyviews.deputy_list_page, name = 'deputy_list_page'),
    # path('deputy/create/', deputyviews.deputy_create_page, name = 'deputy_create_page'),
    # path('ajax/deputy/create/', deputyviews.create_deputy, name = 'ajax_create_deputy'),
    # path('deputy/edit/<int:this_id>/', deputyviews.deputy_edit_page, name = 'deputy_edit_page'),
    # path('ajax/deputy/edit/', deputyviews.edit_deputy, name = 'ajax_edit_deputy'),
    # path('ajax/deputy/delete/', deputyviews.delete_deputy, name = 'ajax_delete_deputy'),
    # Master Data "job group" --------------------------------------------------------------
    # path('job-group/', jobgroupviews.job_group_list_page, name = 'job_group_list_page'),
    # path('job-group/create/', jobgroupviews.job_group_create_page, name = 'job_group_create_page'),
    # path('ajax/job-group/create/', jobgroupviews.create_job_group, name = 'ajax_create_job_group'),
    # path('job-group/edit/<int:this_id>/', jobgroupviews.job_group_edit_page, name = 'job_group_edit_page'),
    # path('ajax/job-group/edit/', jobgroupviews.edit_job_group, name = 'ajax_edit_job_group'),
    # path('ajax/job-group/delete/', jobgroupviews.delete_job_group, name = 'ajax_delete_job_group'),
    # Master Data "personnel" --------------------------------------------------------------
    path('personnel/', personnelviews.personnel_list_page, name = 'personnel_list_page'),
    path('personnel/create/', personnelviews.personnel_create_page, name = 'personnel_create_page'),
    path('ajax/personnel/create/', personnelviews.create_personnel, name = 'ajax_create_personnel'),
#     path('personnel/edit/<str:this_national_code>/', personnelviews.personnel_edit_page, name='personnel_edit_page'),
#     path('api/personnel/edit/<int:pk>/', personnelviews.PersonnelRetrieveUpdate.as_view(),
#          name='api_personnel_edit'),
#     path('personnel/details/<str:this_national_code>/', personnelviews.personnel_details_page,
#          name='personnel_details_page'),
    # path('ajax/personnel/search/', personnelviews.search_in_users, name='ajax_search_in_users'),
    # Master Data "work station" --------------------------------------------------------------
#     path('work-station/', workstationviews.work_station_list_page, name='work_station_list_page'),
#     path('work-station/create/', workstationviews.work_station_create_page, name='work_station_create_page'),
#     path('api/work-station/create/', workstationviews.WorkStationCreate.as_view(), name='api_work_station_create'),
#     path('work-station/edit/<str:this_code>/', workstationviews.work_station_edit_page, name='work_station_edit_page'),
#     path('api/work-station/edit/<int:pk>/', workstationviews.WorkStationRetrieveUpdate.as_view(),
#          name='api_work_station_edit'),
    # Master Data "Contract" --------------------------------------------------------------
#     path('contract/', contractviews.contract_list_page, name = 'contract_list_page'),
#     path('contract/create/', contractviews.contract_create_page, name = 'contract_create_page'),
#     path('api/contract/create/', contractviews.ContractCreate.as_view(), name = 'api_contract_create'),
#     path('contract/edit/<int:this_id>/', contractviews.contract_edit_page, name = 'contract_edit_page'),
#     path('api/contract/edit/<int:pk>/', contractviews.ContractRetrieveUpdate.as_view(), name = 'api_contract_edit'),
    # Master Data "management" --------------------------------------------------------------
#     path('api/management/edit/<int:pk>/', deputyviews.ManagementRetrieveUpdate.as_view(), name='api_management_edit'),

    # Master Data "job title" --------------------------------------------------------------

#     path('api/job-title/edit/<int:pk>/', jobgroupviews.JobTitleRetrieveUpdate.as_view(), name='api_jobtitle_edit'),

    # Master Data "section" --------------------------------------------------------------
#     path('api/section/edit/<int:pk>/', workstationviews.SectionRetrieveUpdate.as_view(),
#          name='api_work_station_edit'),
]
