

from pydantic import BaseModel, validator, ValidationError
from typing import Union

from contentctl.objects.content_base import ContentBase

class UnitTestBaseline(ContentBase):
    name: str
    file: str
    pass_condition: str
    earliest_time: Union[str,None] = None
    latest_time: Union[str,None] = None