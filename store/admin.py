from django.contrib import admin
from .models import User, Category, Product, Order


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name"]
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                ),
            },
        ),
        (
            "Auth Info",
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                ),
            },
        ),
        (
            "Site Info",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )

    readonly_fields = ["email", "password", "date_joined", "last_login"]
    list_display_links = ["username"]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
