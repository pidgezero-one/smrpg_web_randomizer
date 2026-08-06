# Register your models here.

from django.contrib import admin
from .models import Seed, Patch

admin.site.register(Seed)
admin.site.register(Patch)
