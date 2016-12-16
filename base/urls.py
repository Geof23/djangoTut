from django.conf.urls import url

from . import views

app_name = 'base'
urlpatterns = [
    url(r'^download/$', views.DownloadView, name='download'),
    url(r'^accounts/profile/$', views.MainTab.as_view(), name='main'),
    url(r'^$', views.MainTab.as_view(), name='main'),
    url(r'^main/$', views.MainTab.as_view(), name='main'),
    url(r'^attend/$', views.AttendTab.as_view(), name='attend'),
    url(r'^feedb/$', views.FeedbTab.as_view(), name='feedb'),
    #url(r'^org/$', views.OrgTab.as_view(), name='org'),
    url(r'^reg/$', views.RegTab.as_view(), name='reg'),
    url(r'^prog/$', views.ProgTab.as_view(), name='prog'),
    #url(r'^venue/$', views.VenueTab.as_view(), name='venue'),
]
