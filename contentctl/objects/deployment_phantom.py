
from pydantic import Extra, validator, ValidationError

from contentctl.objects.content_base import ContentBase


class DeploymentPhantom(ContentBase):
    cam_workers : str
    label : str
    phantom_server : str
    sensitivity : str
    severity : str
