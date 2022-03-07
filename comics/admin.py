from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Comic

admin.site.site_header = settings.PROJECT_NAME.title()
admin.site.index_title = "Administration"


class ComicAdmin(admin.ModelAdmin):
    model = Comic
    ordering = ("issue_number",)
    exclude = ("issue_number",)
    list_display = (
        "issue",
        "year_released",
        "key_issue",
        "own",
        "own_slabbed",
        "slab_grade",
    )
    search_fields = ["issue_number"]
    readonly_fields = ("issue_cover",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "year_released",
                    "issue_cover",
                    "key_issue",
                    "own",
                    "own_slabbed",
                    "slab_grade",
                    "notes",
                ),
            },
        ),
        ("Extra Controls", {"classes": ("collapse",), "fields": ("cover",)}),
    )

    list_filter = ("key_issue", "own", "own_slabbed", "slab_grade", "year_released")

    @classmethod
    def issue(cls, obj):
        return str(obj)

    @classmethod
    def issue_cover(cls, obj):
        return mark_safe(
            f"""<a href="{obj.cover.url}"><img src="{obj.cover.url}" width="150" /></a>"""
        )


# Register your models here.

admin.site.register(Comic, ComicAdmin)
