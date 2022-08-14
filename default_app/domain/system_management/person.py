"""
    ToDo: DocString
"""
from django.db import models
from django.db.models import Q
from default_app.domain.named_entity import NamedEntity
from common_library.general import BasicSearchParameters


class Person(NamedEntity):
    """ ToDo: DocString """
    last_name = models.CharField(max_length = 100, default = None)

    @classmethod
    def filter(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        page_size = basic_search_parameters.page_size
        offset = (basic_search_parameters.current_page - 1) * basic_search_parameters.page_size

        return cls.objects.filter(Q(name__icontains = basic_search_parameters.filter_value) |
                                    Q(last_name__icontains = basic_search_parameters.filter_value)
                                    ).order_by(
                                        "last_name", "name", "-created_at", "-modified_at"
                                        )[offset : offset + page_size]

    @classmethod
    def total_count(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        return cls.objects.filter(
            Q(name__icontains = basic_search_parameters.filter_value) |
            Q(last_name__icontains = basic_search_parameters.filter_value)).count()
