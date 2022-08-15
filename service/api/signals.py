from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import django.dispatch

from api.models import Mailing, Client, Message

@receiver(post_save, sender=Mailing)
def perform_mailing(sender, instance, created, **kwargs):
    if created:
        print("Perform mailing")
        
        if timezone.now() >= instance.datetime_start and timezone.now() < instance.datetime_end:
            print("Time is bounds")
            
            clients = Client.objects.filter(phone_code=instance.filter)
            messages = []
            # creating message for each client
            for client in clients:
                new_message = Message(datetime=timezone.now(), mailing=instance, client=client)
                new_message.save()
                messages.append(new_message)
                
            # perfomimg mailing of messages
            for message in messages:
                response = send_notification(message.client.phone)
                message.is_sent = True


def send_notification(number):
    print("Send mail function")
    
    send_mail(
    'Рассылка',
    f'Рассылка на номер {number}',
    'from@example.com',
    ['olenkaa.pavlova.20000@gmail.com'],
    fail_silently=False,)
    
    
time_come = django.dispatch.Signal()
        