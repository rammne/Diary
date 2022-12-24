from django.contrib import admin
from .models import Entry

admin.site.register(Entry)
admin.site.site_header = "My Activities"
admin.site.site_title = "My Activities"
