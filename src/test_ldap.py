from ad.ldap_collector import LDAPCollector


def main():
    collector = LDAPCollector(
        server_ip="192.168.56.10",
        username="SHADOWPATH\\Administrator",
        password="Password123!",
        base_dn="DC=shadowpath,DC=local"
    )

    collector.connect()

    print("\nUsers Found:\n")

    users = collector.get_users()

    for user in users:
        print(f"{user.sAMAccountName} ({user.cn})")

    print("\nGroups Found:\n")

    groups = collector.get_groups()

    for group in groups:
        print(f"{group.sAMAccountName} ({group.cn})")


if __name__ == "__main__":
    main()