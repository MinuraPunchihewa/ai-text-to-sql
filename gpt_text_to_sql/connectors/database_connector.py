from typing import Optional
from abc import ABC, abstractmethod


class DatabaseConnector(ABC):
    def __int__(self, name: str, connection_data: Optional[dict]):
        self.name = name
        self.connection_data = connection_data

    @abstractmethod
    def get_tables(self):
        raise NotImplementedError

    @abstractmethod
    def get_columns(self, table_name):
        raise NotImplementedError
