from django.apps import apps as django_apps
from django.views.generic.base import ContextMixin


class RegisteredSubjectViewMixin(ContextMixin):
    """Adds the subject_identifier to the context.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subject_identifier = None

    registered_subject_model = 'edc_registration.registeredsubject'

    @property
    def registered_subject_cls(self):
        return django_apps.get_model(self.registered_subject_model)

    @property
    def registered_subject_obj(self):
        return self.registered_subject_cls.objects.get(
            subject_identifier=self.subject_identifier)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.subject_identifier = self.kwargs.get('subject_identifier')
        context.update(
            subject_identifier=self.subject_identifier,
            gender=self.registered_subject_obj.gender,
            dob=self.registered_subject_obj.dob,
            initials=self.registered_subject_obj.initials,
            identity=self.registered_subject_obj.identity,
            firstname=self.registered_subject_obj.first_name,
            lastname=self.registered_subject_obj.last_name)
        return context
