from django.urls import path, include
from api.viewsets import MailingViewSet, ClientViewSet, StatisticsViewSet, ItemStatisticsViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'client', ClientViewSet,  basename="client")
router.register(r'mailing', MailingViewSet,  basename="mailing")


urlpatterns = [
    path('statistics/', StatisticsViewSet.as_view()),
    path('statistics/<int:id>/', ItemStatisticsViewSet.as_view()),
]
