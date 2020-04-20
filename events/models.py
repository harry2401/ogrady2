from django.db                              import models
from django.utils                           import timezone
from django.conf                            import settings
from django.contrib.auth                    import get_user_model
from django.urls                            import reverse


class Event(models.Model):
  e_date            = models.DateField ('Date of the event, in the format "dd/mm/yy", e.g. for 31st December 2020, enter "31/12/20"', default=timezone.now)
  detail_private    = models.TextField                              ('Details of event', blank=True,null=True)
  created_date      = models.DateTimeField                          (default=timezone.now)
  is_live           = models.BooleanField                           (default=True)
  def __str__(self):
    return self.detail_public
