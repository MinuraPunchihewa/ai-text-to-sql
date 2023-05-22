from typing import Optional, Dict, Text

from .mysql_connector import MySQLConnector


class MariaDB(MySQLConnector):
    """
    The Connector class for MariaDB databases.

    Parameters:
    -----------
    connection_data : Dict
        A dictionary containing the configuration parameters for the MariaDB connection.
        The following keys are required:
            - user: The username to connect to the database.
            - password: The password to connect to the database.
            - host: The host name or IP address of the database server.
            - port: The port number of the database server.
            - database: The name of the database to connect to.

    """
    name = 'MariaDB'

    def __init__(self, connection_data: Optional[Dict]):
        super().__init__(connection_data)