"""
acute - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'acute.schema'
    flow_module   = 'acute.flow'
    javascripts   = [
        'js/acute/routes.js',
        'js/opal/controllers/discharge.js'
    ]