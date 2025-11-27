







from rest_framework.routers import SimpleRouter

from applications.checker.viewsets import FileViewSet


checker_router = SimpleRouter()

checker_router.register('files', FileViewSet, basename='files')