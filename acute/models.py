"""
acute models.
"""
from django.db.models import fields

from opal import models

class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass

class Clerking(models.EpisodeSubrecord):
    _icon = 'fa fa-user'
    
    referrer   = fields.CharField(max_length=200, blank=True, null=True)
    clerked_by = fields.CharField(max_length=200, blank=True, null=True)
    consultant = fields.CharField(max_length=200, blank=True, null=True)

class Plan(models.EpisodeSubrecord):
    _is_singleton = True
    _icon = 'fa fa-list-ol'

    plan = fields.TextField(blank=True, null=True)

class Rescuscitation(models.EpisodeSubrecord):
    _icon = 'fa fa-warning'

    status = fields.CharField(max_length=200, blank=True, null=True)
    
