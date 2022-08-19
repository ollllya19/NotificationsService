from __future__ import absolute_import, unicode_literals
from django.utils import timezone
from django.core.mail import send_mail

from api.models import Client, Message, Mailing
from service.celery import app


@app.task()
def perform_mailing(mailing_id):
    instance = Mailing.objects.get(id=mailing_id)
    if timezone.now() >=  instance.datetime_start and timezone.now() < instance.datetime_end:
            
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

    """send_mail(
        'Рассылка',
        f'Рассылка на номер {number}',
        'from@example.com',
        ['olenkaa.pavlova.20000@gmail.com'],
        fail_silently=False,
    ) """

    