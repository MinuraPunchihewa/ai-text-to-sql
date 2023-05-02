from typing import Optional, Dict, Text
from sqlalchemy import create_engine, inspect
from .database_connector import DatabaseConnector


class SQLiteConnector(DatabaseConnector):
    name = 'SQLite'

    def __init__(self, name: Text, connection_data: Optional[Dict]):
        super().__init__(name, connection_data)

        engine = create_engine(f'sqlite:///{self.connection_data["db_file"]}')
        self.inspector = inspect(engine)

    def get_tables(self):
        return self.inspector.get_table_names()

    def get_columns(self, table_name):
        return self.inspector.get_columns(table_name)