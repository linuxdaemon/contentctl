
from contentctl.objects.config import ConfigDetectionConfiguration
import pytest

def test_bad_schedule():
    with pytest.raises(ValueError):
        deployment = ConfigDetectionConfiguration.parse_obj({
            'scheduling': {
                'cron_schedule': 'foo',
                'earliest_time': '-24h@h',
                'latest_time': 'now',
                'schedule_window': 'auto'
            },
            'notable': {
                'rule_title': 'specific title',
                'rule_description': 'desc',
                'nes_fields': []
            }
        })

def test_good_schedule():
    deployment = ConfigDetectionConfiguration.parse_obj({
        'scheduling': {
            'cron_schedule': '*/5 * * * *',
            'earliest_time': '-24h@h',
            'latest_time': 'now',
            'schedule_window': 'auto'
        },
        'notable': {
            'rule_title': 'specific title',
            'rule_description': 'desc',
            'nes_fields': []
        }
    })
