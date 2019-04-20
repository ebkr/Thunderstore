from django.contrib import admin


from repository.models import Package
from repository.models import PackageVersion


class PackageVersionInline(admin.StackedInline):
    model = PackageVersion
    readonly_fields = (
        "date_created",
        # "description",  # TODO: Add to package, and make that modifiable
        "downloads",
        "file",
        "icon",
        "name",
        # "readme",  # TODO: Add to package, and amek that modifiable
        "version_number",
        "website_url",
        "website_url",
    )
    extra = 0
    filter_horizontal = ("dependencies",)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    inlines = [
        PackageVersionInline,
    ]

    readonly_fields = (
        "date_created",
        "downloads",
        "maintainers",
        "name",
        "owner",
    )
    list_display = (
        "name",
        "owner",
        "is_active",
        "is_pinned",
    )
    list_filter = (
        "is_active",
        "is_pinned",
    )
