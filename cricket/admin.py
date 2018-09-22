from django.contrib import admin

# Register your models here.

from .models import Match_Regi
from .models import Go_Live

admin.site.register(Match_Regi)
admin.site.register(Go_Live)

