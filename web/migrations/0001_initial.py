# Generated by Django 4.2.2 on 2024-02-23 06:24

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('clinic_name', models.CharField(blank=True, max_length=128, null=True)),
                ('physician_name', models.CharField(blank=True, max_length=128, null=True)),
                ('physician_contact', models.CharField(blank=True, max_length=128, null=True)),
                ('patiant_first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('patiant_last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('patiant_dob', models.CharField(blank=True, max_length=128, null=True)),
                ('patiant_phone', models.CharField(blank=True, max_length=128, null=True)),
                ('chief_complaint', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('consultant_note', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Consultation Report',
                'verbose_name_plural': ('Consultation Reports',),
                'db_table': 'web_consultation_reports',
                'ordering': ('-created_at',),
            },
        ),
    ]