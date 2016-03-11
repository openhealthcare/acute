# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allergies',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='allergies',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_allergies_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='allergies',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='allergies',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_allergies_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='clerking',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clerking',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_clerking_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='clerking',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clerking',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_clerking_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_demographics_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_demographics_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_diagnosis_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_diagnosis_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='dischargedue',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dischargedue',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_dischargedue_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='dischargedue',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dischargedue',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_dischargedue_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_investigation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investigation',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_investigation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_location_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_location_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='nursingnotes',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nursingnotes',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_nursingnotes_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='nursingnotes',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nursingnotes',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_nursingnotes_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='pastmedicalhistory',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pastmedicalhistory',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_pastmedicalhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='pastmedicalhistory',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pastmedicalhistory',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_pastmedicalhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_plan_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_plan_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='rescuscitation',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rescuscitation',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_rescuscitation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='rescuscitation',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rescuscitation',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_rescuscitation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='created_by',
            field=models.ForeignKey(related_name='created_acute_treatment_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_acute_treatment_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
