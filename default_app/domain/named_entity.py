"""
    ToDo: DocString
"""
from django.db import models
from django.db.models import Q
from common_library.general import BasicSearchParameters
from default_app.domain.basic_entity import BasicEntity


class NamedEntity(BasicEntity):
    """ ToDo: DocString """
    name = models.CharField(max_length = 100, default = None)

    class Meta:
        """ ToDo: DocString """
        abstract = True

    @classmethod
    def filter(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        page_size = basic_search_parameters.page_size
        offset = (basic_search_parameters.current_page - 1) * basic_search_parameters.page_size

        return cls.objects.filter(Q(uid__icontains = basic_search_parameters.filter_value) |
                                    Q(name__icontains = basic_search_parameters.filter_value)
                                    ).order_by(
                                        "name", "-created_at", "-modified_at"
                                    )[offset : offset + page_size]

    @classmethod
    def total_count(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        return cls.objects.filter(Q(uid__icontains = basic_search_parameters.filter_value) |
                                    Q(name__icontains = basic_search_parameters.filter_value)).count()
