from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

class ReviewAdmin(admin.ModelAdmin):
    search_fields=['subject']

admin.site.register(Review,ReviewAdmin)
