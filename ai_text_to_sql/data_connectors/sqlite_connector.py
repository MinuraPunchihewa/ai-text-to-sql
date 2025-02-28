from typing import Optional, Text

from sqlalchemy import Engine, create_engine
from sqlalchemy.exc import SQLAlchemyError

from ai_text_to_sql.exceptions import (
    ConnectionCreationException,
    InsufficientParametersException,
)

from .data_connector import DataConnector


class SQLiteConnector(DataConnector):
    """
    The Connector class for SQLite databases.

    Parameters:
    -----------
    connection_string : Text
        A SQLAlchemy connection string for the SQLite database.
        This parameter is optional, but either this parameter or the database parameter
        must be specified.
    database : Text
        The path to the SQLite database file.
        This parameter is optional, but either this parameter or the connection_string
        parameter must be specified.
    """

    name = "SQLite"

    def __init__(
        self, connection_string: Optional[Text] = None, database: Optional[Text] = None
    ) -> None:
        if not connection_string and not database:
            raise InsufficientParametersException(
                "Either the connection_string or the database parameter must be "
                "specified."
            )

        self.connection_string = connection_string
        self.database = database
        super().__init__()

    def create_connection(self) -> Engine:
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
            raise ConnectionCreationException(
                f"Could not create connection to SQLite database: {e}"
            )

    def get_connection_string(self) -> Text:
        """
        Get the connection string for the SQLite database.
        :return: The connection string for the SQLite database.
        """
        return (
            self.connection_string
            if self.connection_string
            else f"sqlite:///{self.database}"
        )
