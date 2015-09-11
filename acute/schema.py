"""
Define acute schemas.
"""
from acute import models

list_columns = [
    models.Demographics,
    models.Location,
    models.Diagnosis,
    models.PastMedicalHistory,
    models.Investigation,
    models.Plan,
    models.Rescuscitation
]

list_columns_take = [
    models.Demographics,
    models.Location,
    models.Clerking,
    models.Diagnosis,
    models.PastMedicalHistory,
    models.Plan,
    models.Rescuscitation
]

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

list_schemas = {
    'default': list_columns,
    'take': {
        'default': list_columns_take
    },
    'cardiology': {
        'default': list_columns_specialist_teams
    },
    'respiratory': list_columns_specialist_teams
}

detail_columns = list_columns
