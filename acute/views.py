"""
Views for OPAL acute plugin
"""
from django.views.generic import TemplateView

from opal.core.views import LoginRequiredMixin
from opal import models

class DischargeAcuteModalTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'modals/acute_take_discharge_modal.html'

    def get_context_data(self, **kwargs):
        context = super(DischargeAcuteModalTemplateView, self).get_context_data(**kwargs)
        context['teams'] = models.Team.for_user(self.request.user)
        return context
