from django.urls import path, include

from equity.views import ScriptView

urlpatterns = [
    path('script', ScriptView.as_view())
]