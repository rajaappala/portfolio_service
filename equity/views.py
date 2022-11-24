import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from equity.constants import APPLICATION_JSON_CONTENT_TYPE
from equity.services.service import ScriptService


class ScriptView(APIView):
    renderer_classes = [JSONRenderer]

    def get():
        pass

    def post(self, request, *args, **kwargs):
        try:
            service = ScriptService()
            return HttpResponse(json.dumps(service.save_script_data(request)), content_type = APPLICATION_JSON_CONTENT_TYPE)
        except:
            return HttpResponse(json.dumps({'status': 500}), content_type = APPLICATION_JSON_CONTENT_TYPE)
