from typing import Optional, Dict, Text
from .database_connector import DatabaseConnector
from sqlalchemy import create_engine, inspect, text


class SQLiteConnector(DatabaseConnector):
    name = 'SQLite'

    def __init__(self, name: Text, connection_data: Optional[Dict]):
        super().__init__(name, connection_data)

        self.engine = create_engine(f'sqlite:///{self.connection_data["db_file"]}')
        self.inspector = inspect(self.engine)

    def get_tables(self):
        return self.inspector.get_table_names()

    def get_columns(self, table_name):
        return self.inspector.get_columns(table_name)

    def query(self, query: Text):
        return self.engine.execute(text(query)).fetchall()