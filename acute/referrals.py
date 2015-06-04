"""
Referral routes for OPAL acute
"""
from referral import ReferralRoute

from acute import models


class ClerkingRoute(ReferralRoute):
    name         = 'Acute Take'
    description  = 'Add a patient to the Acute Take list'
    page_title   = 'Acute Admissions'
    target_teams = ['take']
    success_link = '/#/list/take'
    verb = 'Book in'
    progressive_verb = 'Booking in'
    past_verb = 'Booked in'

    # def post_create(self, episode, user):
    #     """
    #     Auto Populate clerked by
    #     """
    #     name = user.first_name[:1] + ' ' + user.last_name
    #     models.Clerking.objects.create(episode=episode, clerked_by=name)
    #     return
        
