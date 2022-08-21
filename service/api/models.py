from django.db import models


class Mailing(models.Model):
    datetime_start = models.DateTimeField()
    message = models.CharField(max_length=1000)
    filter = models.CharField(max_length=3, default='987')
    datetime_end = models.DateTimeField()
    
    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.id}: {self.datetime_start} -- {self.filter} -- {self.datetime_end}"


class Client(models.Model):
    phone = models.CharField(max_length=11)
    phone_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=10)
    time_zone = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.id}: {self.phone_code} -- {self.phone}"

        
        
class Message(models.Model):
    datetime = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, related_name="id_mailing")
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="id_client")
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-id"]
    
    def __str__(self):
        return f"{self.id}: {self.datetime} -- {self.is_sent} -- {self.mailing.id} -- {self.client.id}"
