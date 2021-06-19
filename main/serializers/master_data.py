from rest_framework.serializers import ModelSerializer, SerializerMethodField
from main.models import User, Executive_Device
from django.shortcuts import reverse
from datetime import datetime
import jdatetime

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# user base information 
class UserBaseSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'national_code'
        ]
        read_only_fields = [
            'id',
            'first_name',
            'last_name',
            'national_code'
        ]


# executive_device information 
class ExecutiveDeviceSerializer(ModelSerializer):
    class Meta:
        model = Executive_Device
        fields = [
            'id',
            'title',
            'code',
        ]
        read_only_fields = [
            'id',
            'title',
            'code',
        ]


# # personnel information 
# class PersonnelSerializer(ModelSerializer):
#     full_name = SerializerMethodField('get_full_name')
#     company = SerializerMethodField('get_company_title')
#     relevant_deputy = SerializerMethodField('get_user_relevant_deputy')
#     relevant_unit = SerializerMethodField('get_user_relevant_unit')
#     class Meta:
#         model = User
#         fields = [
#             'id',
#             'full_name',
#             'national_code',
#             'mobile',
#             'role',
#             'company',
#             'relevant_deputy',
#             'relevant_unit',
#             'active'
#         ]
#         read_only_fields = [
#             'id',
#             'full_name',
#             'national_code',
#             'mobile',
#             'role',
#             'company',
#             'relevant_deputy',
#             'relevant_unit',
#             'active'
#         ]
#     def get_full_name(self, this_user):
#         return this_user.get_fullname()
#     def get_company_title(self, this_user):
#         return this_user.company.title
#     def get_user_relevant_deputy(self, this_user):
#         return this_user.get_relevant_deputy()
#     def get_user_relevant_unit(self, this_user):
#         return this_user.get_relevant_unit()


# # committee information 
# class CommitteeSerializer(ModelSerializer):
#     class Meta:
#         model = Committee
#         fields = [
#             'id',
#             'title'
#         ]
#         read_only_fields = [
#             'id',
#             'title'
#         ]


# # recall information 
# class RecallSerializer(ModelSerializer):
#     class Meta:
#         model = Recall
#         fields = [
#             'id',
#             'title',
#             'fk_committee'
#         ]
#         read_only_fields = [
#             'id',
#             'title',
#             'fk_committee'
#         ]


# # subject information 
# class SubjectSerializer(ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = [
#             'id',
#             'title'
#         ]
#         read_only_fields = [
#             'id',
#             'title'
#         ]


# # activity information 
# class ActivitySerializer(ModelSerializer):
#     user_fullname = SerializerMethodField('get_user_fullname')
#     start_date = SerializerMethodField('convert_startdate_to_jalali')
#     end_date = SerializerMethodField('convert_enddate_to_jalali')
#     done_date = SerializerMethodField('convert_donedate_to_jalali')
#     executor_file = SerializerMethodField('get_executor_file')
#     class Meta:
#         model = Activity
#         fields = [
#             'title',
#             'user_fullname',
#             'start_date',
#             'end_date',
#             'percentage',
#             'activity_output',
#             'done_date',
#             'executor_description',
#             'executor_file',
#             'activity_status',
#         ]
#         read_only_fields = [
#             'title',
#             'user_fullname',
#             'start_date',
#             'end_date',
#             'percentage',
#             'activity_output',
#             'executor_description',
#             'executor_file',
#             'done_date',
#             'activity_status',
#         ]
#     def get_user_fullname(self, this_activity):
#         return this_activity.fk_user.get_fullname()
#     def convert_startdate_to_jalali(self, this_activity):
#         date_format = "%Y-%m-%d"
#         thisdate = datetime.strptime(str(this_activity.startdate), date_format)
#         return jdatetime.date.fromgregorian(day = thisdate.day, month = thisdate.month, year = thisdate.year).strftime("%Y/%m/%d")
#     def convert_enddate_to_jalali(self, this_activity):
#         date_format = "%Y-%m-%d"
#         thisdate = datetime.strptime(str(this_activity.enddate), date_format)
#         return jdatetime.date.fromgregorian(day = thisdate.day, month = thisdate.month, year = thisdate.year).strftime("%Y/%m/%d")
#     def convert_donedate_to_jalali(self, this_activity):
#         if this_activity.date_done_activity is not None:
#             date_format = "%Y-%m-%d"
#             thisdate = datetime.strptime(str(this_activity.date_done_activity), date_format)
#             return jdatetime.date.fromgregorian(day = thisdate.day, month = thisdate.month, year = thisdate.year).strftime("%Y/%m/%d")
#         else:
#             return None
#     def get_executor_file(self, this_activity):
#         if this_activity.executor_file is not None:
#             return this_activity.executor_file.url
#         else:
#             return None


# class WebRecallSerializer(ModelSerializer):
#     url = SerializerMethodField('get_recall_url')
#     class Meta:
#         model = Recall
#         fields = [
#             'title',
#             'url'
#         ]
#         read_only_fields = [
#             'title',
#             'url'
#         ]
#     def get_recall_url(self, this_recall):
#         return reverse('master_data:recall_details_page', kwargs = {
#             'this_id': this_recall.id,
#         })