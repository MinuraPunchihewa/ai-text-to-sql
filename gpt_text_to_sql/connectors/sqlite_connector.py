from typing import Dict, Text
from .database_connector import DatabaseConnector
from sqlalchemy import create_engine


class SQLiteConnector(DatabaseConnector):
    name = 'SQLite'

    def __init__(self, name: Text, connection_data: Dict):
        super().__init__(name, connection_data)

    def create_connection(self):
        """
        Create a connection to a SQLite database.
        :return: A SQLAlchemy engine object for the connection to the SQLite database.
        """
        return create_engine(f"sqlite:///{self.connection_data['db_file']}")