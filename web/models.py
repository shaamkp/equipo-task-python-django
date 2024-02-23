from django.db import models

from general.models import BaseModel
from ckeditor.fields import RichTextField

class ConsultationReport(BaseModel):
    clinic_name = models.CharField(max_length=128, null=True, blank=True)
    physician_name = models.CharField(max_length=128, null=True, blank=True)
    physician_contact = models.CharField(max_length=128, null=True, blank=True)
    patiant_first_name = models.CharField(max_length=128, null=True, blank=True)
    patiant_last_name = models.CharField(max_length=128, null=True, blank=True)
    patiant_dob = models.CharField(max_length=128, null=True, blank=True)
    patiant_phone = models.CharField(max_length=128, null=True, blank=True)
    chief_complaint = RichTextField(null=True, blank=True)
    consultant_note = RichTextField(null=True, blank=True)


    class Meta:
        db_table = 'web_consultation_reports'
        verbose_name = "Consultation Report"
        verbose_name_plural = "Consultation Reports"
        ordering = ('-created_at',)
    

    def __str__(self):
        return self.clinic_name
