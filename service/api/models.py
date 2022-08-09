from django.db import models


class Mailing(models.Model):
    id = models.BigIntegerField(primary_key=True)
    datetime_start = models.DateTimeField()
    message = models.CharField(max_length=1000)
    filter = models.CharField(max_length=3)
    datetime_end = models.DateTimeField()
    
    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"
        ordering = ["-id"]


class Client(models.Model):
    id = models.BigIntegerField(primary_key=True)
    phone = models.CharField(max_length=11)
    phone_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=10)
    time_zone = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["-id"]
        
        
class Message(models.Model):
    id = models.BigIntegerField(primary_key=True)
    datetime = models.DateTimeField()
    is_sent = models.BooleanField()
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name="id_mailing")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="id_client")
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-id"]