from django.contrib import admin

from equity.models import Script, ScriptDetail
# Register your models here.

admin.site.register(Script)
admin.site.register(ScriptDetail)