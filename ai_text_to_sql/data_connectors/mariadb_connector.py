from typing import Text, Optional

from .mysql_connector import MySQLConnector


class MariaDBConnector(MySQLConnector):
    """
    The Connector class for MariaDB databases.

    Parameters:
    -----------
    connection_string : Text
        A SQLAlchemy connection string for the MySQL database. This parameter is optional, but either this parameter or
        the user, password, host, port and database parameters must be specified.
    user : Text
        The username to connect to the database. This parameter is optional, but either this parameter (in combination
        with the password, host, port and database parameters) or the connection_string parameter must be specified.
    password : Text
        The password to connect to the database. This parameter is optional, but either this parameter (in combination
        with the user, host, port and database parameters) or the connection_string parameter must be specified.
    host : Text
        The host name or IP address of the database server. This parameter is optional, but either this parameter (in
        combination with the user, password, port and database parameters) or the connection_string parameter must be
        specified.
    port : int
        The port number of the database server. This parameter is optional, but either this parameter (in combination
        with the user, password, host and database parameters) or the connection_string parameter must be specified.
    database : Text
        The name of the database to connect to. This parameter is optional, but either this parameter (in combination
        with the user, password, host and port parameters) or the connection_string parameter must be specified.

    """
    name = 'MariaDB'

    def __init__(self, connection_string: Optional[Text] = None, user: Optional[Text] = None,
                 password: Optional[Text] = None, host: Optional[Text] = None, port: int = None,
                 database: Optional[Text] = None):
        super().__init__(connection_string, user, password, host, port, database)