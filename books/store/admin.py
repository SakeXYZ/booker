from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass