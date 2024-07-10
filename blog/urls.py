from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet,CommentsViewSet

router=DefaultRouter()

router.register(r'blog',BlogViewSet)
router.register(r'blog/(?P<blog_id>[^/]+)/comments',CommentsViewSet)

urlpatterns = [
    path('',include(router.urls)),
    #path('api-token-auth/',Custom)
]
