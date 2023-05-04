import pyodbc
from typing import Optional, Dict, Text
from .database_connector import DatabaseConnector
from sqlalchemy import create_engine, inspect, text


class MSSQLConnector(DatabaseConnector):
    name = 'MSSQL'

    def __init__(self, name: Text, connection_data: Optional[Dict]):
        super().__init__(name, connection_data)

        connection_string = f"mssql+pyodbc://{self.connection_data['user']}:{self.connection_data['password']}@{self.connection_data['host']}:{self.connection_data['port']}/{self.connection_data['database']}"
        try:
            driver = pyodbc.drivers()[-1]
        except IndexError:
            raise Exception("No MSSQL driver found. Please install a driver for MSSQL.")

        self.engine = create_engine(f"{connection_string}?driver={driver}")
        self.inspector = inspect(self.engine)

    def get_tables(self):
        return self.inspector.get_table_names()

    def get_columns(self, table_name):
        return [column['name'] for column in self.inspector.get_columns(table_name)]

    def query(self, query: Text):
        with self.engine.connect() as conn:
            result = conn.execute(text(query))
        return result.fetchall()