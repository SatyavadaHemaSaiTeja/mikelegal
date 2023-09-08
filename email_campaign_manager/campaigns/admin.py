from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'status')
    list_filter = ['status', ]
    search_fields = ('email', 'first_name')
    actions = ['deactivate_selected']

    def deactivate_selected(self, request, queryset):
        queryset.update(status='inactive')

    deactivate_selected.short_description = "Inactive selected subscribers"
