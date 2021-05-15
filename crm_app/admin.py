from django.contrib import admin
from .models import *



admin.site.site_header = 'CRM Dashboard'
admin.site.site_title = 'CRM Dashboard'

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)