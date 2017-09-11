from rest_framework import routers
from rest_api.views import *

router = routers.DefaultRouter()

router.register('user', UserViews, base_name='api-user')
router.register('img', ImgViews, base_name='api-img')
router.register('blog', BlogView, base_name='api-blog')
router.register('article', ArticleView, base_name='api-article')
router.register('category', CategoryView, base_name='api-category')
router.register('tag', TagView, base_name='api-tag')
api_patterns = []
api_patterns += router.urls