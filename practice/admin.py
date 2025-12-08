from django.contrib import admin
from .models import SampleModel

# Register your models here.

@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)