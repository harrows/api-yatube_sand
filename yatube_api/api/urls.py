from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = "api"

router_v1 = DefaultRouter()
router_v1.register(r"posts", PostViewSet, basename="posts")
router_v1.register(r"groups", GroupViewSet, basename="groups")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    re_path(
        r"^v1/posts/(?P<post_id>\d+)/comments/$",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="comments-list",
    ),
    re_path(
        r"^v1/posts/(?P<post_id>\d+)/comments/(?P<pk>\d+)/$",
        CommentViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }),
        name="comments-detail",
    ),
]
