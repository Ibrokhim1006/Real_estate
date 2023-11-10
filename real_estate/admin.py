from django.contrib import admin
from real_estate.models import (
    Currency,
    Region,
    Status,
    Distric,
    CategoriesRealEstet,
    AdType,
    AdSubCategory,
    Repair,
    BuildMaterial,
    Price,
    Amenities,
    NumberRooms,
    RealEstate,
    RealEstetImgaes,
)

admin.site.register(Currency)
admin.site.register(Region)
admin.site.register(Status)


class NewDistric(admin.ModelAdmin):
    model = Distric
    list_display = ["id", "name", "region_id"]


admin.site.register(Distric, NewDistric)
admin.site.register(CategoriesRealEstet)


class NewAdType(admin.ModelAdmin):
    model = AdType
    list_display = ["id", "name", "id_category"]


admin.site.register(AdType, NewAdType)

admin.site.register(AdSubCategory)
admin.site.register(Repair)
admin.site.register(Price)
admin.site.register(Amenities)
admin.site.register(NumberRooms)


class NewRealEstate(admin.ModelAdmin):
    model = RealEstate
    list_display = ["id", "author_id", "distric_id"]


admin.site.register(RealEstate, NewRealEstate)
admin.site.register(RealEstetImgaes)
admin.site.register(BuildMaterial)
