from typing import Text, Optional

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from .data_connector import DataConnector

from ai_text_to_sql.exceptions import ConnectionCreationException, InsufficientParametersException


class MySQLConnector(DataConnector):
    """
    The Connector class for MySQL databases.

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
    name = 'MySQL'

    def __init__(self, connection_string: Optional[Text] = None, user: Optional[Text] = None,
                 password: Optional[Text] = None, host: Optional[Text] = None, port: int = None,
                 database: Optional[Text] = None):
        if not connection_string and not user and not password and not host and not port and not database:
            raise InsufficientParametersException("Either the connection_string or the user, password, host, port and "
                                                  "database parameters must be specified.")
        self.connection_string = connection_string
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        super().__init__()

    def create_connection(self):
        """
        Create a connection to a MySQL database.
        :return: A SQLAlchemy engine object for the connection to the MySQL database.
        """
        try:
            if self.connection_string:
                return create_engine(self.connection_string)
            else:
                return create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/"
                                     f"{self.database}")
        except SQLAlchemyError as e:
            ConnectionCreationException(f"Could not create connection to MySQL database: {e}")
