from django.contrib import admin
from registration.models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'year', 'email')


admin.site.register(Registration, RegistrationAdmin)
