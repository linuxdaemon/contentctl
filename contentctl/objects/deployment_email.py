
from pydantic import Extra, validator, ValidationError

from contentctl.objects.content_base import ContentBase


class DeploymentEmail(ContentBase):
    message: str
    subject: str
    to: str
