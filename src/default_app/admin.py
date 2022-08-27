"""
    ToDo: DocString
"""
from django.contrib import admin
from default_app.domain.system_management import (
    Person, ErrorLog)


# Register your models here.
admin.site.register(Person)
admin.site.register(ErrorLog)
