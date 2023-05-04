from typing import Optional, Dict, Text
from .database_connector import DatabaseConnector
from sqlalchemy import create_engine


class SQLiteConnector(DatabaseConnector):
    name = 'SQLite'

    def __init__(self, name: Text, connection_data: Optional[Dict]):
        super().__init__(name, connection_data)

    def create_connection(self):
        return create_engine(f"sqlite:///{self.connection_data['db_file']}")