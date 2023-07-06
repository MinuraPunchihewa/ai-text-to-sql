from typing import Text

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from .data_connector import DataConnector

from ai_text_to_sql.exceptions import ConnectionCreationException


class SQLiteConnector(DataConnector):
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

    def __init__(self, database: Text):
        self.database = database
        super().__init__()

    def create_connection(self):
        """
        Create a connection to a SQLite database.
        :return: A SQLAlchemy engine object for the connection to the SQLite database.
        """
        try:
            return create_engine(f"sqlite:///{self.database}")
        except SQLAlchemyError as e:
            ConnectionCreationException(f"Could not create connection to SQLite database: {e}")