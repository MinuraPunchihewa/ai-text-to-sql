from typing import Optional, Text, Dict
from gpt_text_to_sql.connectors import *
from .database_connector import DatabaseConnector


class DatabaseConnectorFactory:
    @staticmethod
    def build_connector(name: str, connection_data: Optional[Dict]) -> DatabaseConnector:
        return globals()[f"{name}Connector"](name, connection_data)