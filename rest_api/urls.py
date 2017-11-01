from rest_framework import routers
from rest_api.views import *

router = routers.DefaultRouter()

router.register('user', UserViews, base_name='api-user')
router.register('article', ArticleView, base_name='api-article')
router.register('category', CategoryView, base_name='api-category')
router.register('tag', TagView, base_name='api-tag')
router.register('sign', SignView, base_name='api-sign')
api_patterns = []
api_patterns += router.urls