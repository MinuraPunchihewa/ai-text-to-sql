from typing import Dict, Text
from .database_connector import DatabaseConnector
from sqlalchemy import create_engine


class SQLiteConnector(DatabaseConnector):
    """
    The Connector class for SQLite databases.

    Parameters:
    -----------
    name : str
        The name of the connector.
    connection_data : Dict
        A dictionary containing the configuration parameters for the SQLite connection.
        The following keys are required:
            - database: The path to the SQLite database file.
    """
    name = 'SQLite'

    def __init__(self, name: Text, connection_data: Dict):
        super().__init__(name, connection_data)

    def create_connection(self):
        """
        Create a connection to a SQLite database.
        :return: A SQLAlchemy engine object for the connection to the SQLite database.
        """
        try:
            return create_engine(f"sqlite:///{self.connection_data['database']}")
        except KeyError:
            raise ValueError("Missing parameter in connection_data: database.")