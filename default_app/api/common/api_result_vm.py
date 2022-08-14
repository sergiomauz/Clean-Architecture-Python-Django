"""
    ToDo: DocString
"""
from dataclasses import dataclass


@dataclass
class ApiResultVm:
    """ ToDo: DocString """
    status_code: int = 200
    is_exception: bool = False
    style: str = ""
