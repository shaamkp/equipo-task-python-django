from django.contrib import admin
from web.models import ConsultationReport


class ConsultationReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinic_name', 'physician_name', 'physician_contact', 'patiant_first_name', 'patiant_last_name', 'patiant_dob', 'patiant_phone', 'chief_complaint', 'consultant_note')
    search_fields = ('clinic_name', 'physician_name', 'patiant_first_name', 'patiant_phone',)

admin.site.register(ConsultationReport, ConsultationReportAdmin)
