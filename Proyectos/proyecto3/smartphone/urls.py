from django.urls import path, include
from smartphone import views
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from smartphone.viewsets import ManufacturerViewSet, SmartphoneViewSet

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet)
router.register(r'smartphone', SmartphoneViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Smartphones API",
      default_version='v1',
      description="Api for view smartphone and manufacturers ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns=[
    path('list_manufacturers', views.list_smartphone, name="list_manufacturers"),
    path('register_smartphone/', views.create_smartphone, name="register_smartphone"),
    path('companies/create/', views.create_companies, name="create_companies"),
    path('api/v1/', include(router.urls)),
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # Esto genera documentación automatica.
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]