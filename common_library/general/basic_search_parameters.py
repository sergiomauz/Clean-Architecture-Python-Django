"""
    ToDo: DocString
"""
from typing import Any
from common_library.validators import DeferredValidator


class BasicSearchParameters(DeferredValidator):
    """ ToDo: DocString """
    current_page: int
    page_size: int
    filter_value: str

    @classmethod
    def new(cls, request: Any = None):
        """ ToDo: DocString """
        current_page = request.GET.get("current_page", 1)
        page_size = request.GET.get("page_size", 25)
        filter_value = request.GET.get("filter_value", "")

        new_instance = cls.create_instance(current_page = current_page,
                                           page_size = page_size,
                                           filter_value = filter_value)

        return new_instance.validate()
