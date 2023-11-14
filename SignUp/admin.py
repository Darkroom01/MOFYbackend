from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('userID', 'email', 'name', 'birthdate', 'gen', 'nickname', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('userID', 'email', 'password')}),
        ('Personal info', {'fields': ('name', 'birthdate', 'gen', 'nickname')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('userID', 'email', 'name', 'birthdate', 'gen', 'nickname', 'password1', 'password2')}
         ),
    )
    search_fields = ('userID',)
    ordering = ('userID',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
