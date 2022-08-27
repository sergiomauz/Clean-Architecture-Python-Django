"""
    ToDo: DocString
"""
from pydantic import validator
from common_library.validators import DeferredValidator


class GetPersonQuery(DeferredValidator):
    """ ToDo: DocString """
    uid:str

    @classmethod
    def new(cls, requested_uid: str):
        """ ToDo: DocString """
        new_instance = cls.create_instance(uid = requested_uid)

        return new_instance.validate()
