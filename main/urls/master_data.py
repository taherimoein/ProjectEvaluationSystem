from main.views.master_data import personnelviews , projectviews , organizationviews ,projectstypeviews
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
    path('personnel/edit-<str:username>/', personnelviews.personnel_edit_page, name = 'personnel_edit_page'),
    #path('ajax/personnel/edit-<int:pk>/', personnelviews.PersonnelRetrieveUpdate.as_view(), name = 'ajax_personnel_edit'),
    path('personnel/details-<str:username>/', personnelviews.personnel_details_page, name = 'personnel_details_page'),
    path('ajax/personnel/search/', personnelviews.search_in_users, name = 'ajax_search_in_users'),
    path('personnel/confirmation-of-information-<str:username>/', personnelviews.personnel_confirmation_of_information_page, name = 'personnel_confirmation_of_information_page'),
    path('ajax/personnel/confirmation-of-information/', personnelviews.confirmation_of_information_personnel, name = 'ajax_confirmation_of_information_personnel'),
    # Master Data "project" --------------------------------------------------------------
    path('project/', projectviews.project_list_page, name = 'project_list_page'),
    path('project/create/', projectviews.project_create_page, name = 'project_create_page'),
    path('ajax/project/create/', projectviews.create_project, name = 'ajax_create_project'),
    # Master Data "organization" --------------------------------------------------------------
    path('organizations/', organizationviews.organization_list_page, name='organization_list_page'),
    path('organization/create/', organizationviews.organization_create_page, name='organization_create_page'),

    # Master Data "projects types" --------------------------------------------------------------
    path('projectstype/', projectstypeviews.projectstype_list_page, name='projectstype_list_page'),
    path('projectstype/create/', projectstypeviews.projectstype_create_page, name='projectstype_create_page'),
]
