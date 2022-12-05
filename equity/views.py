import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from equity.serializer import ScriptDetailSerializer, ScriptSerializer
from equity.models import Script, ScriptDetail


class ScriptViewSet(ModelViewSet):
    serializer_class = ScriptSerializer
    queryset = Script.objects.all()


class ScriptDetailsViewSet(ModelViewSet):
    serializer_class = ScriptDetailSerializer
    queryset = ScriptDetail.objects.all()