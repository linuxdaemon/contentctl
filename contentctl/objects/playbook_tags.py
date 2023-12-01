
from pydantic import Extra, validator, ValidationError

from contentctl.objects.content_base import ContentBase


class PlaybookTag(ContentBase):
    analytic_story: list = None
    detections: list = None
    platform_tags: list = None
    playbook_fields: list = None
    product: list = None
    playbook_fields: list = None
    detection_objects: list = None  
    