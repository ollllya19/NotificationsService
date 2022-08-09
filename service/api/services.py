import json
from pickle import TRUE
from tkinter.messagebox import NO
import requests
from rest_framework import status
from rest_framework.response import Response

from api.repositories import MailingRepository
from api.serializers  import MailingSerializer
from api.models import Mailing, Message
from api.serializers import StatisticsSerializer


class MailingViewSetService:

    __slots__ = 'request',

    def __init__(self, request=None):
        self.request = request
        
    def get_statistics(self):
        queryset = Mailing.objects.all()
        serializer = StatisticsSerializer(queryset, many=True)
        return Response(serializer.data)
            
    def get_item_statistics(self):
        item = None
        try:
            item = Mailing.objects.get(id=self.request)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = StatisticsSerializer(item)
            return Response(serializer.data)
