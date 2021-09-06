from django.urls.conf import include
from rest_framework import routers
from django.urls import path
from .views import *
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'FlashExs',FlashFillExecutionList,basename='FlashExs')



#urlpatterns = router.urls

urlpatterns = [
    url(r'sessions/', FlashFillExecutionList.as_view()),

]
urlpatterns += router.urls


