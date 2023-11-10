""" Django Libraries """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentications.models import CustomUser, PyemntSumm
from authentications.forms import ChangeUser, CreasteUser


class NewMyUser(UserAdmin):
    """New User"""

    add_form = CreasteUser
    form = ChangeUser
    model = CustomUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "id",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {"fields": ("avatar", "email_code", "summ", )},
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {"fields": ("avatar", "email_code", "summ", )},
        ),
    )


admin.site.register(CustomUser, NewMyUser)
admin.site.register(PyemntSumm)
