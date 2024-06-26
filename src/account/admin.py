from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccontAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    list_display = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

admin.site.register(Account, AccontAdmin)