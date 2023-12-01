from contentctl.objects.content_base import ContentBase
from contentctl.objects.constants import *


class DetectionSuppression(ContentBase):
    enabled: bool = False
    fields: list[str] = []
    window: str = "86400s"
