from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from . import views


router = DefaultRouter()

router.register('posts', views.PostViewset, basename='posts')
post_router = NestedDefaultRouter(router, r'posts', lookup='posts')
post_router.register(r'comments', views.CommentViewset, basename='comments')


urlpatterns = router.urls
