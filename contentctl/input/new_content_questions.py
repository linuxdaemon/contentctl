import os

from contentctl.helper.utils import DURATION_RE
from contentctl.objects.enums import (
    AnalyticsType,
    DataModel,
    DetectionStatus,
    KillChainPhases,
    NotableSeverity,
    SecurityDomains,
)


def _check_int(min_value=None, max_value=None):
    def _check(v):
        if isinstance(v, str):
            if not v or not v.isdigit():
                return False
            v = int(v)

        if min_value is not None:
            if v <= min_value:
                return False

        if max_value is not None:
            if v > max_value:
                return False

        return True

    return _check


class NewContentQuestions:
    @classmethod
    def get_questions_detection(self) -> list:
        questions = [
            {
                "type": "text",
                "message": "enter detection name",
                "name": "detection_name",
                "default": "Powershell Encoded Command",
            },
            {
                "type": "text",
                "message": "enter detection description",
                "name": "description",
                "multiline": True,
                "validate": lambda desc: len(desc.strip()) > 0,
            },
            {
                "type": "text",
                "message": "enter author name",
                "name": "detection_author",
                "default": os.getenv("USER"),
            },
            {
                "type": "select",
                "message": "select a detection type",
                "name": "detection_type",
                "choices": [a_type.value for a_type in AnalyticsType],
                "default": AnalyticsType.TTP.value,
            },
            {
                "type": "select",
                "message": "Select a lifecycle status",
                "name": "detection_status",
                "choices": [status.name for status in DetectionStatus],
                "default": DetectionStatus.experimental.name,
            },
            {
                "type": "checkbox",
                "message": "select the datamodels used in the detection",
                "name": "datamodels",
                "choices": [
                    model.value
                    for model in DataModel
                ],
                "default": DataModel.Endpoint.value,
            },
            {
                "type": "text",
                "message": "enter search (spl)",
                "name": "detection_search",
                "default": "| UPDATE_SPL",
                "multiline": True,
            },
            {
                "type": "confirm",
                "message": "Do you want to add a throttling configuration?",
                "name": "enable_throttling",
                "default": True,
            },
            {
                "type": "text",
                "message": "enter fields to throttle by",
                "name": "throttling_fields",
                "when": lambda answers: answers["enable_throttling"],
                "instruction": "Seperate multiple fields with a comma (,)",
                "filter": lambda fields: fields.split(","),
            },
            {
                "type": "text",
                "message": "how long to throttle for",
                "name": "throttling_window",
                "when": lambda answers: answers["enable_throttling"],
                "instruction": "Duration in NNhNNmNNs format",
                "default": "1d",
                "validate": lambda duration: DURATION_RE.match(duration) is not None,
            },
            {
                "type": "confirm",
                "message": "Do you want to add a drilldown search?",
                "name": "use_drilldown",
                "default": False,
            },
            {
                "type": "text",
                "message": "enter drilldown name",
                "name": "drilldown_name",
                "when": lambda answers: answers["use_drilldown"],
                "default": "View Contributing Events",
            },
            {
                "type": "text",
                "message": "enter drilldown search (spl) (supports variables)",
                "name": "drilldown_search",
                "when": lambda answers: answers["use_drilldown"],
                "multiline": True,
            },
            {
                "type": "text",
                "message": "enter MITRE ATT&CK Technique IDs related to the detection, comma delimited for multiple",
                "name": "mitre_attack_ids",
                "default": "T1003.002",
            },
            {
                "type": "checkbox",
                "message": "select kill chain phases related to the detection",
                "name": "kill_chain_phases",
                "choices": [
                    phase.value
                    for phase in KillChainPhases
                ],
                "default": KillChainPhases.Exploitation.value,
            },
            {
                "type": "select",
                "message": "security_domain for detection",
                "name": "security_domain",
                "choices": [
                    domain.value
                    for domain in SecurityDomains
                ],
                "default": SecurityDomains.endpoint.value,
            },
            {
                "type": "select",
                "message": "Severity",
                "name": "severity",
                "choices": [item.value for item in NotableSeverity],
                "default": NotableSeverity.Medium.value,
            },
            {
                "type": "text",
                "message": "confidence",
                "name": "confidence",
                "default": "50",
                "filter": int,
                "validate": _check_int(0, 100),
            },
            {
                "type": "text",
                "message": "impact",
                "name": "impact",
                "default": "50",
                "filter": int,
                "validate": _check_int(0, 100),
            },
            {
                "type": "confirm",
                "name": "add_observable",
                "message": "Add observable example?",
                "default": False,
            },
            {
                "type": "text",
                "message": "Next steps",
                "name": "next_steps",
                "multiline": True,
            },
        ]
        return questions

    @classmethod
    def get_questions_story(self) -> list:
        questions = [
            {
                "type": "text",
                "message": "enter story name",
                "name": "story_name",
                "default": "Suspicious Powershell Behavior",
            },
            {
                "type": "text",
                "message": "enter author name",
                "name": "story_author",
            },
            {
                "type": "checkbox",
                "message": "select a category",
                "name": "category",
                "choices": [
                    "Adversary Tactics",
                    "Account Compromise",
                    "Unauthorized Software",
                    "Best Practices",
                    "Cloud Security",
                    "Command and Control",
                    "Lateral Movement",
                    "Ransomware",
                    "Privilege Escalation",
                ],
            },
            {
                "type": "select",
                "message": "select a use case",
                "name": "usecase",
                "choices": [
                    "Advanced Threat Detection",
                    "Security Monitoring",
                    "Compliance",
                    "Insider Threat",
                    "Application Security",
                    "Other",
                ],
            },
        ]
        return questions
