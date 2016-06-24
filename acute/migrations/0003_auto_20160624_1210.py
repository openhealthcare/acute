# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0017_auto_20160509_1645'),
        ('acute', '0002_auto_20160311_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demographics',
            old_name='country_of_birth_fk',
            new_name='birth_place_fk',
        ),
        migrations.RenameField(
            model_name='demographics',
            old_name='country_of_birth_ft',
            new_name='birth_place_ft',
        ),
        migrations.RenameField(
            model_name='demographics',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='ethnicity',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='gender',
        ),
        migrations.AddField(
            model_name='demographics',
            name='ethnicity_fk',
            field=models.ForeignKey(blank=True, to='opal.Ethnicity', null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='ethnicity_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='middle_name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='sex_fk',
            field=models.ForeignKey(blank=True, to='opal.Gender', null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='sex_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='surname',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
