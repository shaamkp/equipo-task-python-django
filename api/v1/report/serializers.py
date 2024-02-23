from rest_framework import serializers


class CreateGenerateConsultingReportSerializer(serializers.Serializer):
    clinic_name = serializers.CharField()
    physician_name = serializers.CharField()
    physician_contact = serializers.CharField()
    patiant_first_name = serializers.CharField()
    patiant_last_name = serializers.CharField()
    patiant_dob = serializers.CharField()
    patiant_phone = serializers.CharField()
    chief_complaint = serializers.CharField()
    consultant_note = serializers.CharField()