from ldap3 import Server
from ldap3 import Connection
from ldap3 import ALL


class LDAPCollector:

    def __init__(
            self,
            server_ip,
            username,
            password
    ):
        self.server_ip = server_ip
        self.username = username
        self.password = password

    def connect(self):

        server = Server(
            self.server_ip,
            get_info=ALL
        )

        connection = Connection(
            server,
            user=self.username,
            password=self.password,
            auto_bind=True
        )

        return connection