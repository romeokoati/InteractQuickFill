from django.urls.conf import include
from rest_framework import routers
from django.urls import path
from .views import *
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'QuickExs',QuickFillExecutionList,basename='QuickExs')
router.register(r'QuickExsFilter',QuickFillExecutionListWithFilter,basename='QuickExsFilter')
router.register(r'QuickExsManyBlock',QuickFillExecutionList,basename='QuickExsManyBlock')


#urlpatterns = router.urls

urlpatterns = [
    url(r'sessions/', QuickFillExecutionList.as_view()),
    url(r'sessions/', QuickFillExecutionListWithFilter.as_view()),
    url(r'sessions/', QuickFillExecutionListManyBlock.as_view()),

]
urlpatterns += router.urls