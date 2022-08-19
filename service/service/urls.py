from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.urls import router as mailing_router


router = DefaultRouter()
router.registry.extend(mailing_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('api.urls')),
    path('service/', include(router.urls))
]
