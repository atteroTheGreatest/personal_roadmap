from django.conf.urls import patterns
from django.contrib import admin
from django.conf.urls import url, include

from rest_framework import routers
from .views import (UserViewSet, BoardViewSet, TaskViewSet,
                    GoalViewSet, InitiativeViewSet)



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'initiatives', InitiativeViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
                       url(r'^api/', include(router.urls)),
                       url(r'^api-auth/',
                           include('rest_framework.urls',
                                   namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
)
