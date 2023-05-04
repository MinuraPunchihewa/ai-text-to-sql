from abc import ABC, abstractmethod
from typing import Optional, Text, Dict
from sqlalchemy import inspect, text


class DatabaseConnector(ABC):
    def __init__(self, name: Text, connection_data: Optional[Dict]):
        self.name = name
        self.connection_data = connection_data
        self.connection = self.create_connection()
        self.inspector = self.create_inspector()

    @abstractmethod
    def create_connection(self):
        raise NotImplementedError

    def create_inspector(self):
        return inspect(self.connection)

    def get_tables(self):
        return self.inspector.get_table_names()

    def get_columns(self, table_name):
        return [column['name'] for column in self.inspector.get_columns(table_name)]

    def query(self, query: Text):
        with self.connection.connect() as conn:
            result = conn.execute(text(query))
        return result.fetchall()
