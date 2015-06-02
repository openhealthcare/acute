from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from opal.urls import urlpatterns as opatterns

from acute import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'templates/modals/acute_take_discharge_modal.html',
        views.DischargeAcuteModalTemplateView.as_view()),
)

urlpatterns += opatterns
