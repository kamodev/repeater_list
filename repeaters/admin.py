from django.contrib import admin
from .models import Repeater, RepeaterLocation, RepeaterDigitalModes, RepeaterLinkModes


class RepeaterLocationInlineAdmin(admin.TabularInline):
    model = RepeaterLocation
    extra = 0


class RepeaterLinkModesInlineAdmin(admin.TabularInline):
    model = RepeaterLinkModes
    extra = 0


class RepeaterDigitalModesInlineAdmin(admin.TabularInline):
    model = RepeaterDigitalModes
    extra = 0


class RepeaterAdmin(admin.ModelAdmin):
    model = Repeater
    list_display = ('callsign', 'output_frequency')
    inlines = [RepeaterLocationInlineAdmin, RepeaterDigitalModesInlineAdmin, RepeaterLinkModesInlineAdmin]


admin.site.register(Repeater, RepeaterAdmin)

