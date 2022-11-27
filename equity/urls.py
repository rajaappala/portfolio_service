from rest_framework.routers import SimpleRouter
from equity import views

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register('equity/script', views.ScriptViewSet)
router.register('equity/script-detail', views.ScriptDetailsViewSet)
