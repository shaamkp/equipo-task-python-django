
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/report/', include('api.v1.report.urls', namespace='api_v1_report')),
]
