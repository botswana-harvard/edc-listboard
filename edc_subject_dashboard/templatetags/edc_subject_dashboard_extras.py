from django import template
from edc_appointment.models.appointment import Appointment
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from edc_appointment.constants import IN_PROGRESS_APPT


register = template.Library()


@register.inclusion_tag('edc_subject_dashboard/forms_button.html')
def forms_button(wrapper=None, visit=None, **kwargs):
    """wrapper is an AppointmentModelWrapper.
    """

    visit_pk = visit.id
    if visit_pk:
        btn_color = 'btn-primary'
        title = ''
        fa_icon = 'fa-list-alt'
        href = wrapper.forms_url
        label = "Forms"
        label_fa_icon = 'fa-mail-forward'
        visit_pk = str(visit_pk)
    else:
        btn_color = 'btn-warning'
        title = 'Click to update the visit report'
        fa_icon = 'fa-plus'
        href = visit.href
        label = "Start"
        label_fa_icon = None
    btn_id = f'{label.lower()}_btn_{wrapper.visit_code}_{wrapper.visit_code_sequence}'
    return dict(
        btn_color=btn_color,
        btn_id=btn_id,
        fa_icon=fa_icon,
        href=href,
        label=label,
        label_fa_icon=label_fa_icon,
        title=title,
        visit_code=wrapper.visit_code,
        visit_code_sequence=wrapper.visit_code_sequence,
        visit_pk=visit_pk
    )


@register.inclusion_tag('edc_subject_dashboard/appointment_in_progress.html')
def appointment_in_progress(subject_identifier=None, visit_schedule=None,
                            schedule=None, **kwargs):

    try:
        appointment = Appointment.objects.get(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule.name,
            schedule_name=schedule.name,
            appt_status=IN_PROGRESS_APPT)
    except ObjectDoesNotExist:
        visit_code = None
    except MultipleObjectsReturned:
        qs = Appointment.objects.filter(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule.name,
            schedule_name=schedule.name,
            appt_status=IN_PROGRESS_APPT)
        visit_code = ', '.join([obj.visit_code for obj in qs])
    else:
        visit_code = appointment.visit_code
    return dict(visit_code=visit_code)