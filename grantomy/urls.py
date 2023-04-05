#
# This file is part of pretix (Community Edition).
#
# Copyright (C) 2014-2020 Raphael Michel and contributors
# Copyright (C) 2020-2021 rami.io GmbH and contributors
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General
# Public License as published by the Free Software Foundation in version 3 of the License.
#
# ADDITIONAL TERMS APPLY: Pursuant to Section 7 of the GNU Affero General Public License, additional terms are
# applicable granting you additional permissions and placing additional restrictions on your usage of this software.
# Please refer to the pretix LICENSE file to obtain the full terms applicable to this work. If you did not receive
# this file, see <https://pretix.eu/about/en/license>.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License along with this program.  If not, see
# <https://www.gnu.org/licenses/>.
#

from django.conf.urls import re_path
from django.urls import include, path
# from pretix.api import urls

# from pretix.api.urls import router

from . import views
from . import api

# urls.event_router.register(r'^test', api.GrantomyViewSet, basename='tomy')
# urls.router.register(r'test2222', views.tomytest, basename='tomy' )

from django.conf.urls import url

urlpatterns = [

    # routes app

    re_path(r'^control/organizer/(?P<organizer>[^/]+)/grantomy/configuration$',
            views.ConfigurationView.as_view(),
            name='grantomy.configuration'),
    
    re_path(r'^control/organizer/(?P<organizer>[^/]+)/grantomy$',
            views.ZeusView.as_view(),
            name='grantomy.zeus'),

    re_path(r'^control/organizer/(?P<organizer>[^/]+)/grantomy/(?P<pk>\d+)$',
            views.ZeusDetailView.as_view(),
            name='grantomy.zeus-detail'),

    re_path(r'^control/organizer/(?P<organizer>[^/]+)/grantomy/add$',
            views.ZeusCreateView.as_view(),
            name='grantomy.zeus-add'),

    re_path(r'^control/organizer/(?P<organizer>[^/]+)/grantomy/(?P<customer>[^/]+)/edit$',
            views.CustomerUpdateView.as_view(),
            name='grantomy.zeus.edit'),

    re_path(r'^control/organizer/(?P<organizer>[^/]+)/grantomy/(?P<customer>[^/]+)/anonymize$',
            views.ZeusAnonymizeView.as_view(),
            name='grantomy.zeus.anonymize'),

    # routes for  API

    re_path(r'^api/v1/organizers/(?P<organizer>[^/]+)/grantomy/customers',
            api.GrantomyViewSet.as_view(),
            name='grantomy.api.customers'),

    re_path(r'^api/v1/organizers/(?P<organizer>[^/]+)/grantomy/dni',
            api.GrantomyDNIViewSet.as_view(),
            name='grantomy.api.customer.dni'),

    re_path(r'^api/v1/organizers/(?P<organizer>[^/]+)/grantomy/document',
            api.GrantomyDocumentViewSet.as_view(),
            name='grantomy.api.customer.document'),


    # organizers/(?P<organizer>[^/]+)

]

# orga_router.register(r'test2222', views.tomytest, basename='tomy' )

# print('--------grantomy--------------')
# print(router)
