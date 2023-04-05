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
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from pretix.base.models.customers import Customer
from pretix.base.models.organizer import Organizer

import uuid


def itempicture_upload_to(instance, filename: str) -> str:
    return 'pub/grantomy/item-%s.%s' % (
        str(uuid.uuid4()), filename.split('.')[-1]
    )


class Zeus(Customer):
    title = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('plugins:grantomy:grantomy.zeus', kwargs={'organizer': self.organizer.slug})


class ZeusDni(models.Model):
    title = models.CharField(max_length=100)

    front = models.ImageField(
        verbose_name=_("Product picture"),
        null=True, blank=True, max_length=255,
        upload_to=itempicture_upload_to
    )

    backend = models.ImageField(
        verbose_name=_("Product picture"),
        null=True, blank=True, max_length=255,
        upload_to=itempicture_upload_to
    )


class ZeusDocument(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.BinaryField(editable=True)


class ZeusConfiguration(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=50)
    configuration = models.JSONField()
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
 