from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('base.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^base/', include('base.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
