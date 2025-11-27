from django.contrib import admin
from django.urls import include, path

from applications.checker.urls import checker_router
from applications.users.urls import users_urlpatterns, users_router


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(users_urlpatterns)),

    path('api/', include(checker_router.urls)),
    path('api/', include(users_router.urls)),
]
