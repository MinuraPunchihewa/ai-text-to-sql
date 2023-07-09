from typing import Text, Optional

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from .data_connector import DataConnector

from ai_text_to_sql.exceptions import ConnectionCreationException, InsufficientParametersException


class SQLiteConnector(DataConnector):
    """
    The Connector class for SQLite databases.

    Parameters:
    -----------
    connection_string : Text
        A SQLAlchemy connection string for the SQLite database. This parameter is optional, but either this parameter or
         the database parameter must be specified.
    database : Text
        The path to the SQLite database file. This parameter is optional, but either this parameter or the
        connection_string parameter must be specified.

    """
    name = 'SQLite'

    def __init__(self, connection_string: Optional[Text] = None, database: Optional[Text] = None):
        if not connection_string and not database:
            raise InsufficientParametersException("Either the connection_string or the database parameter must be "
                                                  "specified.")

        self.connection_string = connection_string
        self.database = database
        super().__init__()

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