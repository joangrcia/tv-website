from django.contrib import admin
from copytrade.models import Metatraders
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
class AccountInline(admin.StackedInline):
    model = Metatraders
    can_delete = False
    verbose_name_plural = 'metatrader'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Metatraders)
