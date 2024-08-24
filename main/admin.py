from datetime import datetime, timedelta
import logging
from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as DjangoUserAdmin
)
from django.utils.html import format_html
from django.db.models.functions import TruncDay
from django.db.models import Avg, Count, Min, Sum
from django.urls import path
from django.template.response import TemplateResponse

from . import models

logger = logging.getLogger(__name__)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'in_stock', 'price')
    list_filter = ('active', 'in_stock', 'date_updated')
    list_editable = ('in_stock',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('tags',)
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        return list(self.readonly_fields) + ['slug', 'name']

    def get_prepopulated_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.prepopulated_fields
        else:
            return {}


class DispatchersProductAdmin(ProductAdmin):
    readonly_fields = ('description', 'price', 'tags', 'active')
    prepopulated_fields = {}
    autocomplete_fields = ()


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        return list(self.readonly_fields) + ['slug', 'name']

    def get_prepopulated_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.prepopulated_fields
        else:
            return {}


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', 'product_name')
    readonly_fields = ('thumbnail',)
    search_fields = ('product_name',)
    
    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="%s">' % obj.thumbnail.url)
        return '-'
    
    thumbnail_tag.short_description = 'Thumbnail'
    
    def product_name(self, obj):
        return obj.product.name


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important dates",
            {"fields": ("last_login", "date_joined")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'address1',
        'address2',
        'city',
        'country',
    )
    readonly_fields = ('user',)


class BasketLineInline(admin.TabularInline):
    model = models.BasketLine
    raw_id_fields = ('product',)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'count')
    list_editable = ('status',)
    list_filter = ('status',)
    inlines = (BasketLineInline,)


class OrderLineInline(admin.TabularInline):
    model = models.OrderLine
    raw_id_fields = ('product',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'shipping_country', 'date_added')
    inlines = (OrderLineInline,)
    fieldsets = (
        (None,
            {'fields': (
                'user',
                'status')
            }
        ),
        ('Billing info',
            {'fields': (
                'billing_name',
                'billing_address1',
                'billing_address2',
                'billing_zip_code',
                'billing_city',
                'billing_country')
            }
        ),
        ('Shipping info',
            {'fields': (
                'shipping_name',
                'shipping_address1',
                'shipping_address2',
                'shipping_zip_code',
                'shipping_city',
                'shipping_country')
            }
        ),
    )


class CentralOfficeOrderLineInline(admin.TabularInline):
    model = models.OrderLine
    readonly_fields = ('product',)


class CentralOfficeOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status')
    list_editable = ('status',)
    readonly_fields = ('user',)
    list_filter = ('status', 'shipping_country', 'date_added')
    inlines = (CentralOfficeOrderLineInline,)
    fieldsets = (
        (None,
            {'fields': (
                'user',
                'status')
            }
        ),
        ('Billing info',
            {'fields': (
                'billing_name',
                'billing_address1',
                'billing_address2',
                'billing_zip_code',
                'billing_city',
                'billing_country')
            }
        ),
        ('Shipping info',
            {'fields': (
                'shipping_name',
                'shipping_address1',
                'shipping_address2',
                'shipping_zip_code',
                'shipping_city',
                'shipping_country')
            }
        ),
    )

