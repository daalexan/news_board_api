from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("news", views.PostView)
router.register("users", views.UserView)
router.register("comments", views.CommentView)
router.register("votes", views.VotePostView, basename="vote_post")


urlpatterns = [path("", include(router.urls))]
