from ad.ldap_collector import LDAPCollector


def main():
    collector = LDAPCollector(
        server_ip="192.168.56.10",
        username="SHADOWPATH\\Administrator",
        password="Password123!",
        base_dn="DC=shadowpath,DC=local"
    )

    collector.connect()

    users = collector.get_users()

    print("\nUsers Found:\n")

    for user in users:
        print(
            f"{user.sAMAccountName} ({user.cn})"
        )


if __name__ == "__main__":
    main()