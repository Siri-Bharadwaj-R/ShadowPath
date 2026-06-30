from core.models import Relationship
from ad.ldap_collector import LDAPCollector


class RelationshipBuilder:
    def __init__(
        self,
        collector: LDAPCollector
    ):
        self.collector = collector

    def build(self) -> list[Relationship]:
        memberships = self.collector.get_group_memberships()

        relationships = []

        for membership in memberships:
            relationships.append(
                Relationship(
                    source=membership["member"],
                    target=membership["group"]
                )
            )

        return relationships