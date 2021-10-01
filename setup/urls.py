from django.contrib import admin
from django.urls import path, include
from ground_sensors.views import GroundSensorViewSet
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Ground Sensor API",
        default_version='v1',
        description="API for data acquisition from soil measurement sensors.",
        terms_of_service="#",
        contact=openapi.Contact(email="ailton1626@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('GroundSensor', GroundSensorViewSet, basename='GroundSensor')

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('access/', admin.site.urls),
    path('', include(router.urls)),
    path('doc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
