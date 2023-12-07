import enum


class AnalyticsType(enum.Enum):
    TTP = "TTP"
    anomaly = "Anomaly"
    hunting = "Hunting"
    correlation = "Correlation"


class NotableSeverity(enum.Enum):
    Informational = "informational"
    Low = "low"
    Medium = "medium"
    High = "high"
    Critical = "critical"


class DataModel(enum.Enum):
    Endpoint = "Endpoint"
    Network_Traffic = "Network_Traffic"
    Authentication = "Authentication"
    Change = "Change"
    Change_Analysis = "Change_Analysis"
    Email = "Email"
    Network_Resolution = "Network_Resolution"
    Network_Sessions = "Network_Sessions"
    UEBA = "UEBA"
    Updates = "Updates"
    Vulnerabilities = "Vulnerabilities"
    Web = "Web"
    Endpoint_Processes = "Endpoint_Processes"
    Endpoint_Filesystem = "Endpoint_Filesystem"
    Endpoint_Registry = "Endpoint_Registry"
    Risk = "Risk"
    Splunk_Audit = "Splunk_Audit"


class SecurityContentType(enum.Enum):
    detections = 1
    baselines = 2
    stories = 3
    playbooks = 4
    macros = 5
    lookups = 6
    deployments = 7
    investigations = 8
    unit_tests = 9

class KillChainPhases(enum.Enum):
    Unknown = "Unknown"
    Reconnaissance = "Reconnaissance"
    Weaponization = "Weaponization"
    Delivery = "Delivery"
    Exploitation = "Exploitation"
    Installation = "Installation"
    Command_And_Control = "Command And Control"
    Actions_on_Objectives = "Actions on Objectives"

class SecurityDomains(enum.Enum):
    access = "access"
    endpoint = "endpoint"
    network = "network"
    threat = "threat"
    identity = "identity"
    audit = "audit"

# Bringing these changes back in line will take some time after
# the initial merge is complete
# class SecurityContentProduct(enum.Enum):
#     # This covers ESCU as well as other apps initialized
#     # by splunk_security_content_builder
#     splunk_app = "splunk_app"
#     ba_objects = "ba_objects"
#     json_objects = "json_objects"
class SecurityContentProduct(enum.Enum):
    SPLUNK_APP = 1
    SSA = 2
    API = 3
    CUSTOM = 4

class SigmaConverterTarget(enum.Enum):
    CIM = 1
    RAW = 2
    OCSF = 3
    ALL = 4

class DetectionStatus(enum.Enum):
    production = "production"
    deprecated = "deprecated"
    experimental = "experimental"

class LogLevel(enum.Enum):
    NONE = "NONE"
    ERROR = "ERROR"
    INFO = "INFO"


class AlertActions(enum.Enum):
    notable = "notable"
    rba = "rba"
    email = "email"

class StoryCategory(str,enum.Enum):
    ABUSE = "Abuse"
    ADVERSARY_TACTICS = "Adversary Tactics"
    BEST_PRACTICES = "Best Practices"
    CLOUD_SECURITY = "Cloud Security"
    COMPLIANCE = "Compliance"
    MALWARE = "Malware"
    UNCATEGORIZED = "Uncategorized"
    VULNERABILITY = "Vulnerability"
    

    # The following categories are currently used in
    # security_content stories but do not appear
    # to have mappings in the current version of ES
    # Should they be removed and the stories which
    # reference them updated?
    ACCOUNT_COMPROMSE = "Account Compromise"
    DATA_DESTRUCTION = "Data Destruction"
    LATERAL_MOVEMENT = "Lateral Movement"
    PRIVILEGE_ESCALATION  = "Privilege Escalation"
    RANSOMWARE = "Ransomware"
    UNAUTHORIZED_SOFTWARE = "Unauthorized Software"
  
  

class PostTestBehavior(str, enum.Enum):
    always_pause = "always_pause"
    pause_on_failure = "pause_on_failure"
    never_pause = "never_pause"


class DetectionTestingMode(str, enum.Enum):
    selected = "selected"
    all = "all"
    changes = "changes"


class DetectionTestingTargetInfrastructure(str, enum.Enum):
    container = "container"
    server = "server"


class InstanceState(str, enum.Enum):
    starting = "starting"
    running = "running"
    error = "error"
    stopping = "stopping"
    stopped = "stopped"
