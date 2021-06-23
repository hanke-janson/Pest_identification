from django.contrib import admin
from django.utils.translation import gettext_lazy
from django.contrib.auth.admin import UserAdmin

from apps.uav import models


# # Register your models here.
@admin.register(models.UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),

        (gettext_lazy('用户基本信息'), {'fields': ('birthday', 'address', 'gender', 'mobile')}),

        (gettext_lazy('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                                  'groups', 'user_permissions')}),

        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('username', 'password1', 'password2'), }),
    )


@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name',)


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name',)


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name',)


@admin.register(models.LonLat)
class LonlatAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('longitude', 'latitude')


@admin.register(models.Area)
class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('province', 'city', 'address', 'lonlat')


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name',)


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'code')


@admin.register(models.FaultCode)
class FaultCodeAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'code')


@admin.register(models.UAV)
class UAVAdmin(admin.ModelAdmin):
    def 故障码(self, obj):
        return [code.code for code in obj.fault_code.all()]

    list_per_page = 10
    list_display = ('ma_code', 'ma_type',
                    'area', 'state',
                    'last_time', 'last_content',
                    'startup_time', 'uptime',
                    '故障码', 'director')
