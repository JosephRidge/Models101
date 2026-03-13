from django.contrib import admin
from .models import Mountain, HikeEvent

# Register your models here.
admin.site.register(Mountain)
admin.site.register(HikeEvent)

