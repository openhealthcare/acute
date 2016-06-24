from django.contrib import admin

from opal.admin import TeamAdmin
from opal.models import Team
admin.site.register(Team, TeamAdmin)
