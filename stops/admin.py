from django.contrib import admin
from .models import LigneTrajet, Stop

admin.site.register(Stop)
admin.site.register(LigneTrajet)