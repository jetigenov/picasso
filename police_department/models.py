from django.db import models
from django.utils.translation import gettext_lazy as _


class Calls(models.Model):
    """
    Police Department Calls from victims
    """
    crime_id = models.BigIntegerField(_("Crime ID"), primary_key=True)
    crime_type = models.CharField(_("Crime Type"), max_length=150)
    report_date = models.DateTimeField(_("Report Date"))
    call_date = models.DateTimeField(_("Call Date"))
    offense_date = models.DateTimeField(_("Offense Date"))
    call_time = models.CharField(_("Call Time"), max_length=10)
    call_date_time = models.DateTimeField(_("Call Date Time"))
    disposition = models.CharField(_("Disposition"), max_length=150)
    address = models.CharField(_("Address"), max_length=255)
    city = models.CharField(_("City"), max_length=50)
    state = models.CharField(_("State"), max_length=50)
    agency_id = models.IntegerField(_("Agency ID"))
    address_type = models.CharField(_("Address Type"), max_length=255, blank=True, null=True)
    common_location = models.CharField(_("Common Location"), max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Call"
        verbose_name_plural = "Calls"

    def __str__(self):
        return "Calls"
