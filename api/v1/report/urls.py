from django.urls import re_path
from api.v1.report import views

app_name = "api_v1_report"

urlpatterns = [
    re_path(r'^generate-report/$', views.generate_report,name="generate-report"),
]