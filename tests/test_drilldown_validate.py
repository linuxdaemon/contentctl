from configparser import RawConfigParser
import pathlib
from contentctl.objects.config import Config, ConfigDrilldown, ConfigNotable
from contentctl.objects.deployment import Deployment
from contentctl.objects.deployment_scheduling import DeploymentScheduling
from contentctl.objects.detection import Detection
from contentctl.objects.detection_tags import DetectionTags
from contentctl.objects.enums import SecurityContentType
from contentctl.output.conf_output import ConfOutput
import pytest

def test_drilldown_validate(tmp_path):
    drilldown = ConfigDrilldown(
        name='name',
        search="test",
        earliest_offset='$info_min_time$',
        latest_offset='$info_max_time$',
    )

def test_drilldown_validate_good_number(tmp_path):
    drilldown = ConfigDrilldown(
        name='name',
        search="test",
        earliest_offset=5,
        latest_offset='$info_max_time$',
    )

def test_drilldown_bad_number(tmp_path):
    with pytest.raises(ValueError):
        drilldown = ConfigDrilldown(
            name='name',
            search="test",
            earliest_offset='$info_min_time$',
            latest_offset=-10,
        )

def test_drilldown_validate_bad_str(tmp_path):
    with pytest.raises(ValueError):
        drilldown = ConfigDrilldown(
            name='name',
            search="test",
            earliest_offset='16h',
            latest_offset='32d',
        )
    
    
    
