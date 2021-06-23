from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
router.register(r'languages', views.LanguageViewSet)
router.register(r'hymns', views.HymnViewSet)
router.register(r'hymn_numbers', views.HymnNumberViewSet)
router.register(r'hymn_files', views.HymnFileViewSet)
router.register(r'ads', views.AdViewSet)

# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-token/', obtain_auth_token, name='api_token')
]
