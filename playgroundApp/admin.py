__author__ = 'hails'
from django.contrib import admin
from models import User, Playground, SchoolDistrict, Age, School, UserReview, SafetyFeatures, Features, TransportationFeatures

class UserAdmin(admin.ModelAdmin):
    search_fields = ('UserID',)
class PlaygroundAdmin(admin.ModelAdmin):
    search_fields = ('PlaygroundID',)
class SchoolDistrictAdmin(admin.ModelAdmin):
    search_fields = ('SchoolDistrictID',)
class AgeAdmin(admin.ModelAdmin):
    search_fields = ('AgeID',)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ('SchoolID',)
class UserReviewAdmin(admin.ModelAdmin):
    search_fields = ('ReviewID',)
class SafetyFeaturesAdmin(admin.ModelAdmin):
    search_fields = ('PlaygroundID',)
class TransportationFeaturesAdmin(admin.ModelAdmin):
    search_fields = ('PlaygroundID',)
class FeaturesAdmin(admin.ModelAdmin):
    search_fields = ('PlaygroundID',)

admin.site.register(User, UserAdmin)
admin.site.register(Playground, PlaygroundAdmin)
admin.site.register(SchoolDistrict, SchoolDistrictAdmin)
admin.site.register(Age, AgeAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(UserReview, UserReviewAdmin)
admin.site.register(SafetyFeatures, SafetyFeaturesAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(TransportationFeatures, TransportationFeaturesAdmin)