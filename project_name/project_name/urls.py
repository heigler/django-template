# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = patterns('',  # noqa

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='base.html')),

)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns(
        '', url(r'^__debug__/', include(debug_toolbar.urls)),
    )
