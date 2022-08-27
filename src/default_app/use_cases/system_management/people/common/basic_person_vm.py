"""
    ToDo: DocString
"""
from dataclasses import dataclass
from common_library.general import BasicViewModel


@dataclass
class BasicPersonVm(BasicViewModel):
    """ ToDo: DocString """
    name: str = None
    last_name: str = None
