from typing import Optional, Text, Dict
from abc import ABC, abstractmethod


class DatabaseConnector(ABC):
    def __init__(self, name: Text, connection_data: Optional[Dict]):
        self.name = name
        self.connection_data = connection_data

    @abstractmethod
    def get_tables(self):
        raise NotImplementedError

    @abstractmethod
    def get_columns(self, table_name):
        raise NotImplementedError
