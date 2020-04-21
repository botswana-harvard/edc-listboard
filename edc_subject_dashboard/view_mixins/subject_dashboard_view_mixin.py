from django.views.generic.base import ContextMixin

from edc_action_item.view_mixins import ActionItemViewMixin
from edc_appointment.view_mixins import AppointmentViewMixin
from edc_consent.view_mixins import ConsentViewMixin
from edc_data_manager.view_mixins import DataActionItemsViewMixin
from edc_locator.view_mixins import SubjectLocatorViewMixin
from edc_metadata.view_mixins import MetaDataViewMixin
from edc_visit_schedule.view_mixins import VisitScheduleViewMixin

from .registered_subject_view_mixin import RegisteredSubjectViewMixin
from .subject_visit_view_mixin import SubjectVisitViewMixin



class VerifyRequisitionMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scanning = self.kwargs.get('scanning')
        context.update(scanning=scanning)
        return context


class SpecialForms(ContextMixin):

    special_forms_include_value = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(special_forms_include_value=self.special_forms_include_value)
        return context


class MaternalInfantDashboardLinks(ContextMixin):

    mother_infant_study = False
    infant_links = False
    maternal_links = False
    infant_dashboard_include_value = None
    maternal_dashboard_include_value = None
    infant_subject_dashboard_url = None

    @property
    def infant_registered_subject(self):
        """Returns an infant registered subject.
        """
        return None

    @property
    def infant_birth(self):
        """Returns and infant birth.
        """
        return None

    @property
    def wrapped_infant_birth(self):
        """Return a wrapped infant birth instance.
        """
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            infant_subject_dashboard_url=self.infant_subject_dashboard_url,
            infant_birth=self.infant_birth,
            wrapped_infant_birth=self.wrapped_infant_birth,
            infant_registered_subject=self.infant_registered_subject,
            mother_infant_study=self.mother_infant_study,
            infant_links=self.infant_links,
            maternal_links=self.maternal_links,
            infant_dashboard_include_value=self.infant_dashboard_include_value,
            maternal_dashboard_include_value=self.maternal_dashboard_include_value)
        return context


class SubjectDashboardViewMixin(
        MetaDataViewMixin,
        ConsentViewMixin,
        SubjectLocatorViewMixin,
        AppointmentViewMixin,
        ActionItemViewMixin,
        SubjectVisitViewMixin,
        VisitScheduleViewMixin,
        RegisteredSubjectViewMixin,
        VerifyRequisitionMixin,
        SpecialForms,
        DataActionItemsViewMixin,
        MaternalInfantDashboardLinks):

    pass
