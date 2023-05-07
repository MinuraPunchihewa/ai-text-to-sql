from typing import Optional, Dict, Text
from .database_connector import DatabaseConnector
from sqlalchemy import create_engine


class MySQLConnector(DatabaseConnector):
    name = 'MySQL'

    def __init__(self, name: Text, connection_data: Optional[Dict]):
        super().__init__(name, connection_data)

    def create_connection(self):
        return create_engine(f"mysql+pymysql://{self.connection_data['user']}:{self.connection_data['password']}@{self.connection_data['host']}:{self.connection_data['port']}/{self.connection_data['database']}")