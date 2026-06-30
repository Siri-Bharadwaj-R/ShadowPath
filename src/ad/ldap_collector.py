from typing import Any

from ldap3 import ALL, Connection, Server, SUBTREE
from ldap3.core.exceptions import LDAPException


class LDAPCollector:
    def __init__(
        self,
        server_ip: str,
        username: str,
        password: str,
        base_dn: str
    ) -> None:
        self.server_ip = server_ip
        self.username = username
        self.password = password
        self.base_dn = base_dn
        self.connection: Connection | None = None

    def connect(self) -> Connection:
        try:
            server = Server(
                self.server_ip,
                get_info=ALL
            )

            self.connection = Connection(
                server,
                user=self.username,
                password=self.password,
                auto_bind=True
            )

            print("[+] Connected to Active Directory")

            return self.connection

        except LDAPException as error:
            raise RuntimeError(
                f"Failed to connect to Active Directory: {error}"
            ) from error

    def get_users(self):
        if self.connection is None:
            raise RuntimeError("Not connected to Active Directory.")

        self.connection.search(
            search_base=self.base_dn,
            search_filter="(&(objectClass=user)(objectCategory=person))",
            search_scope=SUBTREE,
            attributes=[
                "cn",
                "sAMAccountName"
            ]
        )

        return self.connection.entries

    def get_groups(self):
        if self.connection is None:
            raise RuntimeError("Not connected to Active Directory.")

        self.connection.search(
            search_base=self.base_dn,
            search_filter="(objectClass=group)",
            search_scope=SUBTREE,
            attributes=[
                "cn",
                "sAMAccountName"
            ]
        )

        return self.connection.entries

    def get_group_memberships(self) -> list[dict[str, Any]]:
        if self.connection is None:
            raise RuntimeError("Not connected to Active Directory.")

        memberships = []

        groups = self.get_groups()

        for group in groups:
            group_name = str(group.cn)

            self.connection.search(
                search_base=group.entry_dn,
                search_filter="(objectClass=group)",
                search_scope="BASE",
                attributes=["member"]
            )

            if not self.connection.entries:
                continue

            members = self.connection.entries[0].member.values

            for member_dn in members:
                self.connection.search(
                    search_base=member_dn,
                    search_filter="(objectClass=*)",
                    search_scope="BASE",
                    attributes=[
                        "objectClass",
                        "cn",
                        "sAMAccountName"
                    ]
                )

                if not self.connection.entries:
                    continue

                entry = self.connection.entries[0]

                object_classes = [
                    cls.lower()
                    for cls in entry.objectClass.values
                ]

                if "group" in object_classes:
                    memberships.append(
                        {
                            "member": str(entry.cn),
                            "group": group_name,
                            "type": "group"
                        }
                    )

                elif "user" in object_classes:
                    memberships.append(
                        {
                            "member": str(entry.sAMAccountName),
                            "group": group_name,
                            "type": "user"
                        }
                    )

        return memberships