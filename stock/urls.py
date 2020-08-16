from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from stock import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'ashokley', views.AshokleyViewSet)
router.register(r'sensex', views.SensexViewSet)
router.register(r'cipla', views.CiplaViewSet)
router.register(r'nifty', views.NiftyViewSet)
router.register(r'reliance', views.RelianceViewSet)
router.register(r'tatasteel', views.TatasteelViewSet)
router.register(r'eichermotors', views.EichermotorsViewSet)
router.register(r'user',views.UserView)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
