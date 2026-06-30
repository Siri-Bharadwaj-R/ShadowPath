from ad.ldap_collector import LDAPCollector
from ad.relationship_builder import RelationshipBuilder


def main():
    collector = LDAPCollector(
        server_ip="192.168.56.10",
        username="SHADOWPATH\\Administrator",
        password="Password123!",
        base_dn="DC=shadowpath,DC=local"
    )

    collector.connect()

    builder = RelationshipBuilder(collector)

    relationships = builder.build()

    print("\nRelationships:\n")

    for relationship in relationships:
        print(
            f"{relationship.source} -> {relationship.target}"
        )


if __name__ == "__main__":
    main()