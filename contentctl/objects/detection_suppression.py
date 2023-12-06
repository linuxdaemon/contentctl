from pydantic import root_validator, validator
from contentctl.helper.utils import DURATION_RE
from contentctl.objects.content_base import ContentBase


class DetectionSuppression(ContentBase):
    enabled: bool = False
    fields: list[str] = []
    window: str = "86400s"

    @root_validator
    def check_empty_fields(cls, values):
        if values["enabled"] and not values["fields"]:
            raise ValueError("Empty fields not allowed when throttling is enabled")

        return values

    @validator("window")
    def check_window(cls, v):
        if not DURATION_RE.match(v):
            raise ValueError(f"Invalid duration: {v}, must match NNdNNhNNmNNs format")

        return v
