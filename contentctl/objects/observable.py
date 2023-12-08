from pydantic import validator
from contentctl.objects.constants import SES_OBSERVABLE_ROLE_MAPPING, SES_OBSERVABLE_TYPE_MAPPING
from contentctl.objects.content_base import ContentBase
from contentctl.objects.enums import ObservableRole, ObservableType


class Observable(ContentBase):
    name: str
    type: ObservableType
    role: list[ObservableRole]
