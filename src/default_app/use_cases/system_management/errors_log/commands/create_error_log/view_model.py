"""
    ToDo: DocString
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CreateErrorLogVm:
    """ ToDo: DocString """
    status_code: int = None
    description: str = None
    stack_trace: str = None
    created_at: datetime = None
