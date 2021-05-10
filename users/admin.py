from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name'] # new
    # fieldsets = UserAdmin.fieldsets + ( # new
    #     (None, {'fields': ('email',)}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + ( # new
    #     (None, {'fields': ('email',)}),
    # )


admin.site.register(CustomUser, CustomUserAdmin)