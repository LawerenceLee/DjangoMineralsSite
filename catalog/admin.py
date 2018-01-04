from django.contrib import admin

from .models import Mineral


class MineralAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Mineral, MineralAdmin)
