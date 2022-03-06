from django.contrib import admin
from django.conf import settings

from .models import Comic

# admin.site.site_url =
admin.site.site_header = settings.PROJECT_NAME
admin.site.index_title = "Administration"


class ComicAdmin(admin.ModelAdmin):
    model = Comic


# class EnvironmentAdmin(admin.ModelAdmin):
#     model = Environment
#     list_display = ("name", "description")


# class DeploymentAdmin(admin.ModelAdmin):
#     model = Deployment
#     list_display = ("id", "deployed_at", "service", "environment", "region")
#     readonly_fields = []

#     list_filter = (
#         "service",
#         "environment",
#         "region",
#     )
#     search_fields = ["service", "environment", "region"]

#     def has_add_permission(self, request):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return False

#     def get_readonly_fields(self, request, obj=None):
#         return (
#             list(self.readonly_fields)
#             + [field.name for field in obj._meta.fields]
#             + [field.name for field in obj._meta.many_to_many]
#         )


# class RegionAdmin(admin.ModelAdmin):
#     model = Region


# class ServiceAdmin(admin.ModelAdmin):
#     model = Service
#     list_display = ("service", "pauseable", "description")
#     search_fields = ["service", "description"]


# Register your models here.

admin.site.register(Comic, ComicAdmin)
