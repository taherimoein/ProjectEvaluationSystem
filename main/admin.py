from .models import User, UserManager, Official_Letter
from django.contrib.auth import get_user_model
from django.contrib import admin

User = get_user_model()
# Main Section Title
admin.site.site_header = 'ProjectEvaluationSystem'
# --------------------------------
# Official_Letter Admin Section
@admin.register(Official_Letter)
class Official_LetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'fk_sender', 'fk_receiver', 'status', 'create_date')
    search_fields = ['title', 'fk_sender', 'fk_receiver', 'description']
    list_filter = ('status',)
    ordering = ['id', 'title', 'create_date']
# User Admin Section
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'national_code', 'mobile', 'access_group', 'superuser', 'staff', 'active', 'create_date')
    search_fields = ['username', 'national_code', 'first_name', 'last_name', 'mobile']
    list_filter = ('access_group', 'active')
    ordering = ['id', 'create_date']
admin.site.register = (User, UserAdmin)
admin.site.register = (UserManager)