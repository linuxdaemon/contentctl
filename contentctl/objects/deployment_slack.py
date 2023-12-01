
from pydantic import Extra, validator, ValidationError

from contentctl.objects.content_base import ContentBase


class DeploymentSlack(ContentBase):
    channel: str
    message: str