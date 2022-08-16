#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from api.serializers import MailingSerializer, ClientSerializer
from api.services import MailingViewSetService
from api.models import Mailing, Client
from api.tasks import perform_task


class MailingViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()


class ClientViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
    
class StatisticsViewSet(APIView):

    def get(self, request):
        return MailingViewSetService().get_statistics()
    
    
class ItemStatisticsViewSet(APIView):
    perform_task.delay()
    def get(self, request, id):
        return MailingViewSetService(id).get_item_statistics()
            
            

