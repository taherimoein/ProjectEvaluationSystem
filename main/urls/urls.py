from main.views import base_views
from django.urls import path

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

app_name = 'main'
urlpatterns = [
    path('', base_views.index_page, name = 'index_page'),
    # sign in path <----------------------------------------------->
    path('signin/', base_views.signin_page, name ='sign_page'),
    path('ajax-signin/', base_views.signin, name = 'ajax_signin'),
    path('signup/', base_views.signup_page , name ='signup_page'),
    path('ajax-signup/', base_views.signup, name = 'ajax_signup'),
    # sign out path <----------------------------------------------->
    path('signout/', base_views.signout, name = 'sign_out_page'),
    # forget password path <----------------------------------------------->
    path('forget-password/', base_views.forget_password_page, name = 'forget_password_page'),
    path('ajax/forget-password/send-validation-code/', base_views.forget_password_send_validation_code, name = 'ajax_forget_password_send_validation_code'),
    path('ajax/forget-password/change-password/', base_views.forget_password_change_password, name = 'ajax_forget_password_change_password'),
]