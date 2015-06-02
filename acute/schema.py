"""
Define acute schemas.
"""
from acute import models

list_columns = [
    models.Demographics,
    models.Location,
    models.Clerking,
    models.PastMedicalHistory,
    models.Diagnosis,
    models.Plan,
    models.Rescuscitation
]

list_schemas = {
    'default': list_columns,
}

detail_columns = list_columns
