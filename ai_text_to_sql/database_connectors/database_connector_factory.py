import sys
import inspect
from typing import Optional, Dict, Type

from ai_text_to_sql.database_connectors import *
from .database_connector import DatabaseConnector


class DatabaseConnectorFactory:
    """
    The class for building database database_connectors.
    """
    @staticmethod
    def build_connector(name: str, connection_data: Optional[Dict]) -> DatabaseConnector:
        """
        Build a database connector.
        :param name: The name of the connector.
        :param connection_data: A dictionary containing the configuration parameters for the database connection.
        :return: A database connector.
        """
        connectors = DatabaseConnectorFactory._discover_connectors()
        if name in connectors:
            return connectors[name](connection_data)
        else:
            raise ValueError(f"Unsupported connector: {name}")

    @staticmethod
    def _discover_connectors() -> Dict[str, Type[DatabaseConnector]]:
        """
        Discover available database_connectors dynamically.
        :return: A dictionary mapping connector names to their corresponding classes.
        """
        connectors = {}
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj) and issubclass(obj, DatabaseConnector) and obj is not DatabaseConnector:
                connectors[obj.__name__[:-9]] = obj  # Remove "Connector" from class name
        return connectors
