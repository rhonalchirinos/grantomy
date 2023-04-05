
from django.forms import models
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

from .models import Zeus
from pretix.base.models.memberships import MembershipType

from pretix.control.forms.organizer import CustomerUpdateForm


class ZeusForm(models.ModelForm):

    class Meta:
        model = Zeus
        fields = ["identifier", "email", "phone", "external_identifier", "notes", "locale", "title", "edad"]


class ZeusUpdateForm(CustomerUpdateForm):

    class Meta:
        model = Zeus
        fields = ['is_active', 'external_identifier', 'name_parts', 'email', 'is_verified', 'phone', 'locale', 'notes', 'title', 'edad']

    def clean(self):
        email = self.cleaned_data.get('email')

        if email is not None:
            try:
                Zeus.objects.exclude(pk=self.instance.pk).get(email=email, organizer_id=self.instance.organizer.pk)
            except Zeus.DoesNotExist:
                pass
            else:
                raise forms.ValidationError(
                    self.error_messages['duplicate'],
                    code='duplicate',
                )

        return self.cleaned_data


class ZeusConfigurationForm(forms.Form):
    membershiptype = forms.ChoiceField(required=True)

    def setOtganizerChoices(self, organizer):
        choices = [(None, "----")]
        membershiptypes = MembershipType.objects.values_list("id", "name", named=True).filter(organizer=organizer)

        for type in membershiptypes:
            choices.append((type.id, type.name))
        self.fields['membershiptype'] = forms.ChoiceField(choices=choices,)
