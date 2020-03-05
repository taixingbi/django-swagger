
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from musics import views


schema_view = get_swagger_view(title='API')

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', schema_view),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
