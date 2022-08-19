from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import Mailing
from api.tasks import perform_mailing

@receiver(post_save, sender=Mailing)
def send_email(sender, instance, created, **kwargs):
    perform_mailing.delay(instance.id)
        