from django.contrib import admin
from django.conf import settings

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

    list_filter = ("key_issue", "own", "own_slabbed", "slab_grade", "year_released")

    # fieldsets = (
    #     (
    #         "General Details",
    #         {
    #             "fields": (
    #                 "year_released",
    #                 "key_issue",
    #                 "own",
    #                 "own_slabbed",
    #                 "slab_grade",
    #                 "notes",
    #             ),
    #         },
    #     ),
    # )

    @classmethod
    def issue(cls, obj):
        return str(obj)


# Register your models here.

admin.site.register(Comic, ComicAdmin)
