"""
Patient Lists for the Acute application
"""
from opal.core import patient_lists

from acute import models

list_columns_specialist_teams = [
    models.Demographics,
    models.Location,
    models.Diagnosis,
    models.PastMedicalHistory,
    models.Plan,
    models.Treatment,
    models.Investigation,
    models.DischargeDue,
]


class TakeList(patient_lists.TaggedPatientList):
    display_name = 'Acute Take'
    tag          = 'take'
    order        = 1
    schema       = [
        models.Demographics,
        models.Location,
        models.Clerking,
        models.Diagnosis,
        models.PastMedicalHistory,
        models.Plan,
        models.Rescuscitation
    ]


class AAUList(patient_lists.TaggedPatientList):
    display_name = 'AAU'
    tag          = 'aau'
    order        = 2
    schema       = [
        models.Demographics,
        models.Location,
        models.Diagnosis,
        models.PastMedicalHistory,
        models.Investigation,
        models.Plan,
        models.Rescuscitation
    ]


class CardiologyList(patient_lists.TaggedPatientList):
    display_name = 'Cardiology'
    tag          = 'cardiology'
    order        = 3
    schema       = list_columns_specialist_teams

class RespiratoryList(patient_lists.TaggedPatientList):
    display_name = 'Respiratory'
    tag          = 'respiratory'
    order        = 4
    schema       = list_columns_specialist_teams
