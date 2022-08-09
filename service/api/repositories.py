from api.models import Mailing


class MailingRepository:

    @staticmethod
    def get_all():
        return Mailing.objects.all()
    
