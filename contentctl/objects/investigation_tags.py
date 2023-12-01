
from pydantic import Extra, validator, ValidationError

from contentctl.objects.content_base import ContentBase


class InvestigationTags(ContentBase):
    analytic_story: list
    product: list
    required_fields: list
    security_domain: str