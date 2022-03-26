from pathlib import Path

from django.conf import settings
from django.contrib import admin
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from .models import Comic, Copy

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
                    "notes",
                ),
            },
        ),
        # ("Extra Controls", {"classes": ("collapse",), "fields": ("cover",)}),
    )

    list_filter = ("key_issue", "year_released")

    @classmethod
    def issue(cls, obj):
        return str(obj)

    @classmethod
    def issue_cover(cls, obj):
        path = f"{settings.STATIC_ROOT}/covers/xmen_{obj.issue_number}.jpg"
        url = static("covers/xmen_100.jpg")
        path = Path(path)

        return (
            mark_safe(f"""<a href="{url}"><img src="{url}" width="150" /></a>""")
            if path.exists()
            else "-"
        )


class CopyAdmin(admin.ModelAdmin):
    model = Copy
    # ordering = ("issue_number",)
    # exclude = ("issue_number",)
    list_display = (
        "comic",
        "slabbed",
        "grade",
    )
    # search_fields = ["issue_number"]
    # readonly_fields = ("issue_cover",)
    # fieldsets = (
    #     (
    #         None,
    #         {
    #             "fields": (
    #                 "year_released",
    #                 "issue_cover",
    #                 "key_issue",
    #                 "notes",
    #             ),
    #         },
    #     ),
    #     ("Extra Controls", {"classes": ("collapse",), "fields": ("cover",)}),
    # )

    # list_filter = ("key_issue", "year_released")

    @classmethod
    def issue(cls, obj):
        return str(obj)


# Register your models here.

admin.site.register(Comic, ComicAdmin)
admin.site.register(Copy, CopyAdmin)
