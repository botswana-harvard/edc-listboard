from django.urls.base import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
from django.urls.exceptions import NoReverseMatch


class ModelAdminSubjectDashboardMixin:

    subject_dashboard_url = 'subject_dashboard_url'

    def dashboard(self, obj=None):

        try:
            
            url = reverse(settings.DASHBOARD_URL_NAMES.get(self.subject_dashboard_url),
                      kwargs=dict(subject_identifier=obj.subject_identifier))
            
        except NoReverseMatch:
            pass
        else:
            return mark_safe(
                f'<a class="button" title="go to subject dashboard" '
                f'href="{url}">{obj.subject_identifier}</a>')
            
    dashboard.short_description = 'Dashboard'
