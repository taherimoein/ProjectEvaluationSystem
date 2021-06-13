from main.views.master_data import personnelviews, projectviews, organizationviews, projectstypeviews
from django.urls import path

# -----------------------------------------------------------------------------------------------------------------------------------

app_name = 'master_data'
urlpatterns = [
    # Master Data "personnel" --------------------------------------------------------------
    path('personnel/', personnelviews.personnel_list_page, name = 'personnel_list_page'),
    path('personnel/create/', personnelviews.personnel_create_page, name = 'personnel_create_page'),
    path('ajax/personnel/create/', personnelviews.create_personnel, name = 'ajax_create_personnel'),
    path('personnel/edit-<str:username>/', personnelviews.personnel_edit_page, name = 'personnel_edit_page'),
    path('ajax/personnel/edit/', personnelviews.edit_personnel, name = 'ajax_edit_personnel'),
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
