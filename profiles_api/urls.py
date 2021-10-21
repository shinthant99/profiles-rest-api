from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, base_name = 'hello_viewset')
###regfisterting viewsel/ queryset ma shi mha base_name nae pay
router.register('profile', views.UserProfileViewSets)
router.register('feed', views.UserProfileFeedViewSet)
###
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
