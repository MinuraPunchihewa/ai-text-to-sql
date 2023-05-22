from typing import Dict, Text

from sqlalchemy import create_engine

from .connector import Connector


class SQLiteConnector(Connector):
    """
    The Connector class for SQLite databases.

    Parameters:
    -----------
    connection_data : Dict
        A dictionary containing the configuration parameters for the SQLite connection.
        The following keys are required:
            - database: The path to the SQLite database file.
    """
    name = 'SQLite'

    def __init__(self, connection_data: Dict):
        super().__init__(connection_data)

    def create_connection(self):
        """
        Create a connection to a SQLite database.
        :return: A SQLAlchemy engine object for the connection to the SQLite database.
        """
        try:
            return create_engine(f"sqlite:///{self.connection_data['database']}")
        except KeyError:
            raise ValueError("Missing parameter in connection_data: database.")