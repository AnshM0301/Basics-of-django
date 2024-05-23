from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from .models import *

class Image(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    # list_display = ['name','image_tag']

admin.site.register(recipe, Image)

admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
