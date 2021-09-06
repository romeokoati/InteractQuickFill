from django.urls.conf import include
from rest_framework import routers
from django.urls import path
from .views import *
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'QuickExs',QuickFillExecutionList,basename='QuickExs')


#urlpatterns = router.urls

urlpatterns = [
    url(r'sessions/', QuickFillExecutionList.as_view()),

]
urlpatterns += router.urls