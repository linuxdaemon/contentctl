
from pydantic import Extra, validator, ValidationError

from contentctl.objects.content_base import ContentBase


class DeploymentNotable(ContentBase):
    rule_description: str
    rule_title: str
    nes_fields: list
