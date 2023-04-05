
from django.http import HttpResponse

from grantomy.models import Zeus, ZeusConfiguration
from django.core.serializers import serialize

from django.shortcuts import render
from django.urls import reverse

from django.views.generic.detail import DetailView
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.functional import cached_property
from django.shortcuts import get_object_or_404
from django.views import View
from django import forms
from django.contrib import messages

from pretix.control.views.organizer import CustomerCreateView, CustomerUpdateView, CustomerAnonymizeView, CustomerListView
from pretix.control.signals import nav_organizer
from pretix.control.forms.filter import CustomerFilterForm

from .forms import ZeusForm, ZeusUpdateForm, ZeusConfigurationForm


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {}
    return render(request, 'pretixplugins/grantomy/zeus.html', context)


class ConfigurationView(View):
    form_class = ZeusConfigurationForm
    template_name = 'grantomy/zeus_configuration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.configuration.configuration)
        form.setOtganizerChoices(self.request.organizer)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs): 
        form = self.form_class(request.POST)
        form.setOtganizerChoices(self.request.organizer)
        if form.is_valid():
            configuration = self.configuration
            configuration.configuration = form.cleaned_data
            configuration.save()
            messages.success(self.request, _('Your changes have been saved.'))
            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})

    @property  
    def configuration(self): 
        (configuration, created ) = ZeusConfiguration.objects.get_or_create(
            key='GRANTOMY_MEMBERSHIPTYPE',
            organizer=self.request.organizer 
        )
        return configuration


class ZeusView(CustomerListView):
    model = Zeus
    template_name = 'grantomy/zeus.html'
    permission = 'can_manage_customers'

    def get_queryset(self):
        qs = self.request.organizer.customers.all()

        qs = Zeus.objects.filter(organizer=self.request.organizer)

        if self.filter_form.is_valid():
            qs = self.filter_form.filter_qs(qs)
        return qs

    @cached_property
    def filter_form(self):
        return CustomerFilterForm(data=self.request.GET, request=self.request)


class ZeusDetailView(DetailView):
    model = Zeus
    template_name = 'grantomy/zeus_detail.html'
    context_object_name = 'customer'

    @cached_property
    def customer(self):
        return get_object_or_404(
            self.request.organizer.customers,
            pk=self.kwargs.get('pk')
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['customer'] = self.customer

        ctx['memberships'] = self.customer.memberships.with_usages().select_related(
            'membership_type', 'granted_in', 'granted_in__order', 'granted_in__order__event'
        )

        for m in ctx['memberships']:
            if m.membership_type.max_usages:
                m.percent = int(m.usages / m.membership_type.max_usages * 100)
            else:
                m.percent = 0

        return ctx




class ZeusCreateView(CustomerCreateView):
    template_name = 'grantomy/zeus_form.html'
    permission = 'can_manage_customers'
    context_object_name = 'customer'
    form_class = ZeusForm

    def get_form_kwargs(self):
        ctx = super().get_form_kwargs()
        c = Zeus(organizer=self.request.organizer)
        c.assign_identifier()
        ctx['instance'] = c
        return ctx

    # def form_valid(self, form):
    #     r = super().form_valid(form)
    #     form.instance.log_action('pretix.customer.created', user=self.request.user, data={
    #         k: getattr(form.instance, k)
    #         for k in form.changed_data
    #     })
    #     messages.success(self.request, _('Your changes have been saved.'))
    #     return r

    def get_success_url(self):
        return reverse('plugins:grantomy:grantomy.zeus-detail', kwargs={
            'organizer': self.request.organizer.slug,
            'pk': self.object.id,
        })


class CustomerUpdateView(CustomerUpdateView):
    template_name = 'grantomy/zeus_edit.html'
    permission = 'can_manage_customers'
    context_object_name = 'customer'
    form_class = ZeusUpdateForm

    def get_object(self, queryset=None):
        return get_object_or_404(
            Zeus,
            identifier=self.kwargs.get('customer')
        )

    def get_success_url(self):
        return reverse('plugins:grantomy:grantomy.zeus-detail', kwargs={
            'organizer': self.request.organizer.slug,
            'pk': self.object.id,
        })


class ZeusAnonymizeView(CustomerAnonymizeView):
    template_name = 'grantomy/zeus_anonymize.html'
    permission = 'can_manage_customers'
    context_object_name = 'customer'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Zeus,
            identifier=self.kwargs.get('customer')
        )

    def get_success_url(self):
        return reverse('plugins:grantomy:grantomy.zeus-detail', kwargs={
            'organizer': self.request.organizer.slug,
            'pk': self.object.id,
        })
