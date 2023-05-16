from typing import Dict, Text

from sqlalchemy import create_engine

from .database_connector import DatabaseConnector


class MySQLConnector(DatabaseConnector):
    """
    The Connector class for MySQL databases.

    Parameters:
    -----------
    name : str
        The name of the connector.
    connection_data : Dict
        A dictionary containing the configuration parameters for the MySQL connection.
        The following keys are required:
            - user: The username to connect to the database.
            - password: The password to connect to the database.
            - host: The host name or IP address of the database server.
            - port: The port number of the database server.
            - database: The name of the database to connect to.

    """
    name = 'MySQL'

    def __init__(self, name: Text, connection_data: Dict):
        super().__init__(name, connection_data)

    def create_connection(self):
        """
        Create a connection to a MySQL database.
        :return: A SQLAlchemy engine object for the connection to the MySQL database.
        """
        try:
            return create_engine(f"mysql+pymysql://{self.connection_data['user']}:{self.connection_data['password']}"
                                 f"@{self.connection_data['host']}:{self.connection_data['port']}/"
                                 f"{self.connection_data['database']}")
        except KeyError as e:
            missing_param = str(e).strip("'")
            raise ValueError(f"Missing parameter in connection_data: {missing_param}.")
