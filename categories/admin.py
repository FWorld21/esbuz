from django.contrib import admin
from .models import *

admin.site.register(Categories)


class PostProductAdmin(admin.StackedInline):
    model = ProductDescription


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostProductAdmin]

    class Meta:
        model = Product
