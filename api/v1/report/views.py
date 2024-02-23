import traceback

from django.db import transaction
from django.template.loader import render_to_string
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny

from weasyprint import HTML

from web.models import *
from api.v1.report.serializers import *
from general.functions import generate_serializer_errors

@api_view(['POST'])
@permission_classes([AllowAny])
def generate_report(request):
    try:
        serialized_data = CreateGenerateConsultingReportSerializer(data=request.data)
        if serialized_data.is_valid():
            clinic_name = request.data["clinic_name"]
            physician_name = request.data["physician_name"]
            physician_contact = request.data["physician_contact"]
            patiant_first_name = request.data["patiant_first_name"]
            patiant_last_name = request.data["patiant_last_name"]
            patiant_dob = request.data["patiant_dob"]
            patiant_phone = request.data["patiant_phone"]
            chief_complaint = request.data["chief_complaint"]
            consultant_note = request.data["consultant_note"]

            report = ConsultationReport.objects.create(
                clinic_name = clinic_name,
                physician_name = physician_name,
                physician_contact = physician_contact,
                patiant_first_name = patiant_first_name,
                patiant_last_name = patiant_last_name,
                patiant_dob = patiant_dob,
                patiant_phone = patiant_phone,
                chief_complaint = chief_complaint,
                consultant_note = consultant_note
            )

            context = {
                "clinic_name" : report.clinic_name,
                "physician_name" : report.physician_name,
                "physician_contact" : report.physician_contact,
                "patiant_first_name" : report.patiant_first_name,
                "patiant_last_name" : report.patiant_last_name,
                "patiant_phone" : patiant_phone,
                "patiant_dob" : patiant_dob,
                "chief_complaint" : report.chief_complaint,
                "consultant_note" : report.consultant_note,
            }

            html_string = render_to_string('generate_report.html', context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="consulting_report.pdf"'

            HTML(string=html_string).write_pdf(response)

            return response


        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : generate_serializer_errors(serialized_data._errors)
                }
            }

    except Exception as E:
        transaction.rollback()
        errType = E.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "StatusCode": 6001,
            "title": "Failed",
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(E),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)



