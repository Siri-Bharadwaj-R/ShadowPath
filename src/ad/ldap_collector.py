from ldap3 import ALL, Connection, Server
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
        """
        Establish an authenticated LDAP connection to Active Directory.
        """

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