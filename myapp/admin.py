from django.contrib import admin

from myapp.models import Consumer, ServiceProvider

admin.site.register(Consumer)
admin.site.register(ServiceProvider)
