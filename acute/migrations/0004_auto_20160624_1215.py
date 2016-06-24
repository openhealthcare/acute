# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def migrate_forwards(apps, schema_editor):
    Demographics = apps.get_model("acute", "Demographics")

    for demographic in Demographics.objects.all():
        names = demographic.first_name.split(" ")

        if len(names) == 1:
            demographic.surname = names[0]
        else:
            demographic.first_name = names[0]
            demographic.surname = " ".join(names[1:])

        demographic.save()


def migrate_backwards(apps, schema_editor):
    Demographics = apps.get_model("acute", "Demographics")

    for demographic in Demographics.objects.all():
        names = [
            demographic.first_name,
            demographic.middle_name,
            demographic.last_name
        ]

        demographic.name = " ".join(i for i in names if i)
        demographic.save()

class Migration(migrations.Migration):

    dependencies = [
        ('acute', '0003_auto_20160624_1210'),
    ]

    operations = [
          migrations.RunPython(
            migrate_forwards, reverse_code=migrate_backwards
        )
    ]
