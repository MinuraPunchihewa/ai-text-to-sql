import pyodbc
from typing import Dict, Text
from .database_connector import DatabaseConnector
from sqlalchemy import create_engine


class MSSQLConnector(DatabaseConnector):
    """
    The Connector class for MSSQL databases.

    Parameters:
    -----------
    name : str
        The name of the connector.
    connection_data : Dict
        A dictionary containing the configuration parameters for the MSSQL connection.
        The following keys are required:
            - user: The username to connect to the database.
            - password: The password to connect to the database.
            - host: The host name or IP address of the database server.
            - port: The port number of the database server.
            - database: The name of the database to connect to.

    """
    name = 'MSSQL'

    def __init__(self, name: Text, connection_data: Dict):
        super().__init__(name, connection_data)

    def create_connection(self):
        """
        Create a connection to a MSSQL database.
        :return: A SQLAlchemy engine object for the connection to the MSSQL database.
        """
        try:
            connection_string = f"mssql+pyodbc://{self.connection_data['user']}:{self.connection_data['password']}@{self.connection_data['host']}:{self.connection_data['port']}/{self.connection_data['database']}"
        except KeyError as e:
            missing_param = str(e).strip("'")
            raise ValueError(f"Missing parameter in connection_data: {missing_param}.")

        try:
            driver = pyodbc.drivers()[-1]
        except IndexError:
            raise Exception("No MSSQL driver found. Please install a driver for MSSQL.")

        return create_engine(f"{connection_string}?driver={driver}")
