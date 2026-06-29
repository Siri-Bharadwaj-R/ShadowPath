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