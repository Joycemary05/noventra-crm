from django.contrib import admin
from .models import Lead, FollowUp

from django.contrib import admin
from .models import Lead, FollowUp


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'company',
        'source',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'source',
    )

    search_fields = (
        'name',
        'email',
        'company',
    )

    ordering = (
        '-created_at',
    )


@admin.register(FollowUp)
class FollowUpAdmin(admin.ModelAdmin):
    list_display = (
        'lead',
        'follow_up_date',
        'created_at',
    )

    list_filter = (
        'follow_up_date',
    )

    search_fields = (
        'lead__name',
        'lead__email',
        'note',
    )

    ordering = (
        '-follow_up_date',
    )