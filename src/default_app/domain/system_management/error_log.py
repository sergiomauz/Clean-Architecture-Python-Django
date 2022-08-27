"""
    ToDo: DocString
"""
from django.db import models
from default_app.domain.basic_entity import BasicEntity


class ErrorLog(BasicEntity):
    """ ToDo: DocString """
    status_code = models.IntegerField(default = 0)
    description = models.CharField(max_length = 1500)
    stack_trace = models.CharField(max_length = 6150)
