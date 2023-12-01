from contentctl.objects.content_base import ContentBase


class DeploymentScheduling(ContentBase):
    cron_schedule: str
    earliest_time: str
    latest_time: str
    schedule_window: str
