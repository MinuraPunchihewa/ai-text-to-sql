from typing import Optional, Dict

from gpt_text_to_sql.connectors import *
from .database_connector import DatabaseConnector


class DatabaseConnectorFactory:
    """
    The class for building database connectors.
    """
    @staticmethod
    def build_connector(name: str, connection_data: Optional[Dict]) -> DatabaseConnector:
        """
        Build a database connector.
        :param name: The name of the connector.
        :param connection_data: A dictionary containing the configuration parameters for the database connection.
        :return: A database connector.
        """
        return globals()[f"{name}Connector"](name, connection_data)