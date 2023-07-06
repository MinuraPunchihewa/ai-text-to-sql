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

    def __init__(self, connection_string: Text = None, database: Text = None):
        self.database = database
        super().__init__(connection_string)

    def create_connection(self):
        """
        Create a connection to a SQLite database.
        :return: A SQLAlchemy engine object for the connection to the SQLite database.
        """
        try:
            if self.connection_string:
                return create_engine(self.connection_string)
            else:
                return create_engine(f"sqlite:///{self.database}")
        except SQLAlchemyError as e:
            ConnectionCreationException(f"Could not create connection to SQLite database: {e}")