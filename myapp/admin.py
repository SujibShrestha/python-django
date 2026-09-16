from django.contrib import admin
from .models import appVariety, appReview, Store, appCertificate

# Register your models here.
class AppReviewInline(admin.TabularInline):
    model = appReview
    extra = 2

class AppVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    inlines = [AppReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('app_varieties',)

class AppCertificateInline(admin.ModelAdmin):
    list_display = ('certificate_number', 'issued_date', 'valid_until')



admin.site.register(appVariety , AppVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(appCertificate, AppCertificateInline)
