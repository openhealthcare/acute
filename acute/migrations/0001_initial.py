# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0003_speciality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('provisional', models.BooleanField(default=False)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('drug_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('drug_fk', models.ForeignKey(blank=True, to='opal.Drug', null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Clerking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('referrer', models.CharField(max_length=200, null=True, blank=True)),
                ('clerked_by', models.CharField(max_length=200, null=True, blank=True)),
                ('consultant', models.CharField(max_length=200, null=True, blank=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('hospital_number', models.CharField(max_length=255, blank=True)),
                ('nhs_number', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('ethnicity', models.CharField(max_length=255, null=True, blank=True)),
                ('gender', models.CharField(max_length=255, null=True, blank=True)),
                ('country_of_birth_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('country_of_birth_fk', models.ForeignKey(blank=True, to='opal.Destination', null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('provisional', models.BooleanField(default=False)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('date_of_diagnosis', models.DateField(null=True, blank=True)),
                ('condition_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('condition_fk', models.ForeignKey(blank=True, to='opal.Condition', null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DischargeDue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('date', models.DateField(null=True, blank=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('test', models.CharField(max_length=255)),
                ('date_ordered', models.DateField(null=True, blank=True)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('microscopy', models.CharField(max_length=255, blank=True)),
                ('organism', models.CharField(max_length=255, blank=True)),
                ('sensitive_antibiotics', models.CharField(max_length=255, blank=True)),
                ('resistant_antibiotics', models.CharField(max_length=255, blank=True)),
                ('result', models.CharField(max_length=255, blank=True)),
                ('igm', models.CharField(max_length=20, blank=True)),
                ('igg', models.CharField(max_length=20, blank=True)),
                ('vca_igm', models.CharField(max_length=20, blank=True)),
                ('vca_igg', models.CharField(max_length=20, blank=True)),
                ('ebna_igg', models.CharField(max_length=20, blank=True)),
                ('hbsag', models.CharField(max_length=20, blank=True)),
                ('anti_hbs', models.CharField(max_length=20, blank=True)),
                ('anti_hbcore_igm', models.CharField(max_length=20, blank=True)),
                ('anti_hbcore_igg', models.CharField(max_length=20, blank=True)),
                ('rpr', models.CharField(max_length=20, blank=True)),
                ('tppa', models.CharField(max_length=20, blank=True)),
                ('viral_load', models.CharField(max_length=20, blank=True)),
                ('parasitaemia', models.CharField(max_length=20, blank=True)),
                ('hsv', models.CharField(max_length=20, blank=True)),
                ('vzv', models.CharField(max_length=20, blank=True)),
                ('syphilis', models.CharField(max_length=20, blank=True)),
                ('c_difficile_antigen', models.CharField(max_length=20, blank=True)),
                ('c_difficile_toxin', models.CharField(max_length=20, blank=True)),
                ('species', models.CharField(max_length=20, blank=True)),
                ('hsv_1', models.CharField(max_length=20, blank=True)),
                ('hsv_2', models.CharField(max_length=20, blank=True)),
                ('enterovirus', models.CharField(max_length=20, blank=True)),
                ('cmv', models.CharField(max_length=20, blank=True)),
                ('ebv', models.CharField(max_length=20, blank=True)),
                ('influenza_a', models.CharField(max_length=20, blank=True)),
                ('influenza_b', models.CharField(max_length=20, blank=True)),
                ('parainfluenza', models.CharField(max_length=20, blank=True)),
                ('metapneumovirus', models.CharField(max_length=20, blank=True)),
                ('rsv', models.CharField(max_length=20, blank=True)),
                ('adenovirus', models.CharField(max_length=20, blank=True)),
                ('norovirus', models.CharField(max_length=20, blank=True)),
                ('rotavirus', models.CharField(max_length=20, blank=True)),
                ('giardia', models.CharField(max_length=20, blank=True)),
                ('entamoeba_histolytica', models.CharField(max_length=20, blank=True)),
                ('cryptosporidium', models.CharField(max_length=20, blank=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('hospital', models.CharField(max_length=255, blank=True)),
                ('ward', models.CharField(max_length=255, blank=True)),
                ('bed', models.CharField(max_length=255, blank=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NursingNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('notes', models.TextField(null=True, blank=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PastMedicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('year', models.CharField(max_length=4, blank=True)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('condition_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('condition_fk', models.ForeignKey(blank=True, to='opal.Condition', null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('plan', models.TextField(null=True, blank=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Rescuscitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('status', models.CharField(max_length=200, null=True, blank=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('dose', models.CharField(max_length=255, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('route_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('drug_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('frequency_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('drug_fk', models.ForeignKey(blank=True, to='opal.Drug', null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('frequency_fk', models.ForeignKey(blank=True, to='opal.Drugfreq', null=True)),
                ('route_fk', models.ForeignKey(blank=True, to='opal.Drugroute', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
    ]
