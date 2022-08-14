"""
    ToDo: DocString
"""
import uuid
from typing import List
from django.db import models
from django.utils import timezone
from common_library.general import BasicSearchParameters
from common_library.utils import convert_to_uuid


class BasicEntity(models.Model):
    """ ToDo: DocString """
    uid = models.UUIDField(primary_key = True, default = uuid.UUID(int = 0))
    created_at = models.DateTimeField(null = False, blank = False)
    modified_at = models.DateTimeField(null = True, blank = True)

    class Meta:
        """ ToDo: DocString """
        abstract = True

    @classmethod
    def get_by_uid(cls, str_uid: str):
        """ ToDo: DocString """
        uid = convert_to_uuid(str_uid)

        if uid is not None:
            try:
                return cls.objects.get(uid = uid)
            except Exception:
                return None

        return None

    @classmethod
    def get_list_by_uids(cls, uids_list: List[str]):
        """ ToDo: DocString """
        return cls.objects.filter(uid__in = uids_list)

    @classmethod
    def filter(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        page_size = basic_search_parameters.page_size
        offset = (basic_search_parameters.current_page - 1) * basic_search_parameters.page_size

        return cls.objects.filter(uid__icontains =
                                    basic_search_parameters.filter_value
                                    ).order_by(
                                        "-created_at", "-modified_at"
                                    )[offset : offset + page_size]

    @classmethod
    def total_count(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        return cls.objects.filter(uid__icontains =
                                    basic_search_parameters.filter_value).count()

    def save(self, *args, **kwargs):
        """ ToDo: DocString """
        if self.uid == uuid.UUID(int = 0):
            self.uid = uuid.uuid1()
            self.created_at = timezone.now()
        else:
            self.modified_at = timezone.now()
        super().save(*args, **kwargs)
