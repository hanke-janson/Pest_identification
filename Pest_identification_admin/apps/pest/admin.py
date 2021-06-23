from django.contrib import admin
from apps.pest import models
from django.contrib.admin import site

site.site_title = "生态监测后台管理系统"
site.site_header = "生态监测后台管理系统"
site.index_title = "生态监测后台管理系统"


# # Register your models here.
@admin.register(models.Orders)
class OrderAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'code')


@admin.register(models.Family)
class FamilyAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'code')


@admin.register(models.Genus)
class GenusAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'code')


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


@admin.register(models.Lonlat)
class LonlatAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('longitude', 'latitude')


@admin.register(models.Area)
class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('province', 'city', 'address', 'lonlat')


@admin.register(models.Crop)
class CropAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name',)


@admin.register(models.Pest)
class PestAdmin(admin.ModelAdmin):

    def 危害庄稼(self, obj):
        return [crop.name for crop in obj.crops.all()]

    def 分布区域(self, obj):
        return [area.address.name for area in obj.areas.all()]

    list_per_page = 10
    list_display = (
        'name', 'code', 'Latin',
        'egg', 'larva', 'pupa', 'adult',
        'order', 'family', 'genus',
        '危害庄稼', '分布区域',
        'encyclopedias'
    )
