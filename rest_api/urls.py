from rest_framework import routers
from rest_api.views import *

router = routers.DefaultRouter()

router.register('user', UserViews, base_name='api-user')
router.register('img', ImgViews, base_name='api-img')
api_patterns = []
api_patterns += router.urls