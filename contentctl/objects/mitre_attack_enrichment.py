from contentctl.objects.content_base import ContentBase


class MitreAttackEnrichment(ContentBase):
    mitre_attack_id: str
    mitre_attack_technique: str
    mitre_attack_tactics: list
    mitre_attack_groups: list
