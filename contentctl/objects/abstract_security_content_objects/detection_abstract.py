from pathlib import Path
import uuid
import string
import requests
import time
import sys

from pydantic import BaseModel, validator, root_validator, Extra
from dataclasses import dataclass
from typing import Union
from datetime import datetime, timedelta
from contentctl.objects.detection_suppression import DetectionSuppression


from contentctl.objects.security_content_object import SecurityContentObject
from contentctl.objects.enums import AnalyticsType
from contentctl.objects.enums import DataModel
from contentctl.objects.enums import DetectionStatus
from contentctl.objects.detection_tags import DetectionTags
from contentctl.objects.config import ConfigDetectionConfiguration, ConfigDrilldown
from contentctl.objects.unit_test import UnitTest
from contentctl.objects.macro import Macro
from contentctl.objects.lookup import Lookup
from contentctl.objects.baseline import Baseline
from contentctl.objects.playbook import Playbook
from contentctl.helper.link_validator import LinkValidator
from contentctl.objects.enums import SecurityContentType
from contentctl.output.new_content_yml_output import NewContentYmlOutput


class Detection_Abstract(SecurityContentObject):
    # internal fields
    file_path: str = None
    contentType: SecurityContentType = SecurityContentType.detections
    
    # Standard fields
    type: AnalyticsType
    status: DetectionStatus
    data_source: list[str] = None
    search: Union[str, dict]
    how_to_implement: str
    known_false_positives: str
    check_references: bool = False
    references: list
    tags: DetectionTags
    throttling: DetectionSuppression = DetectionSuppression()
    tests: list[UnitTest] = []

    # enrichments
    datamodel: list[DataModel] = None
    deprecated: bool = None
    experimental: bool = None
    deployment: ConfigDetectionConfiguration = None
    annotations: dict = None
    risk: list = None
    playbooks: list[Playbook] = None
    baselines: list[Baseline] = None
    mappings: dict = None
    macros: list[Macro] = None
    lookups: list[Lookup] = None
    cve_enrichment: list = None
    splunk_app_enrichment: list = None
    source: str = None
    nes_fields: str = None
    providing_technologies: list = None
    runtime: str = None
    drilldown: ConfigDrilldown = None
    disabled: bool = False

    class Config:
        use_enum_values = True

    # @validator("type")
    # def type_valid(cls, v, values):
    #     if v.lower() not in [el.name.lower() for el in AnalyticsType]:
    #         raise ValueError("not valid analytics type: " + values["name"])
    #     return v

    @validator("how_to_implement")
    def encode_error(cls, v, values, field):
        return SecurityContentObject.free_text_field_valid(cls, v, values, field)

    # @root_validator
    # def search_validation(cls, values):
    #     if 'ssa_' not in values['file_path']:
    #         if not '_filter' in values['search']:
    #             raise ValueError('filter macro missing in: ' + values["name"])
    #         if any(x in values['search'] for x in ['eventtype=', 'sourcetype=', ' source=', 'index=']):
    #             if not 'index=_internal' in values['search']:
    #                 raise ValueError('Use source macro instead of eventtype, sourcetype, source or index in detection: ' + values["name"])
    #     return values

    # disable it because of performance reasons
    # @validator('references')
    # def references_check(cls, v, values):
    #     return LinkValidator.check_references(v, values["name"])
    #     return v

    @validator("search")
    def search_validate(cls, v, values):
        # write search validator
        if file := values.get('file_path'):
            macro = Path(file).name.rsplit('.', 1)[0] + '_filter'
            if not v.strip().endswith(f'| `{macro}`'):
                raise ValueError(f"Missing filter macro: expected {macro}")

        return v

    @validator("tests", always=True)
    def tests_validate(cls, v, values):
        status = DetectionStatus(values.get("status", ""))
        if status != DetectionStatus.production:
            # Not prod, we don't care
            return v

        if 'tags' in values and values["tags"].manual_test:
            # Testing is manual, this is fine
            return v

        if not v:
            raise ValueError(
                "tests value is needed for production detection: " + values["name"]
            )

        return v

    @validator("experimental", always=True)
    def experimental_validate(cls, v, values):
        if DetectionStatus(values.get("status", "")) == DetectionStatus.experimental:
            return True
        return False

    @validator("deprecated", always=True)
    def deprecated_validate(cls, v, values):
        if DetectionStatus(values.get("status", "")) == DetectionStatus.deprecated:
            return True
        return False

    def all_tests_successful(self) -> bool:
        if (
            len(self.tests) == 0
            and self.status == DetectionStatus.production.value
            and not self.tags.manual_test
        ):
            return False
        for test in self.tests:
            if test.result is None or test.result.success == False:
                return False
        return True

    def get_summary(
        self,
        detection_fields: list[str] = ["name", "search"],
        test_model_fields: list[str] = ["success", "message"],
        test_job_fields: list[str] = ["resultCount", "runDuration"],
    ) -> dict:
        summary_dict = {}
        for field in detection_fields:
            summary_dict[field] = getattr(self, field)
        summary_dict["success"] = self.all_tests_successful()
        summary_dict["tests"] = []
        for test in self.tests:
            result: dict[str, Union[str, bool]] = {"name": test.name}
            if test.result is not None:
                result.update(
                    test.result.get_summary_dict(
                        model_fields=test_model_fields,
                        job_fields=test_job_fields,
                    )
                )
            else:
                result["success"] = False
                result["message"] = "RESULT WAS NONE"

            summary_dict["tests"].append(result)

        return summary_dict
