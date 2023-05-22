from abc import ABC, abstractmethod
from typing import Text, Dict, List, Any

import sqlalchemy
from sqlalchemy import inspect, text


class Connector(ABC):
    """
    The abstract base class for database connectors.

    Parameters
    ----------
    name: Text
        The name of the connector.
    connection_data: Dict
        A dictionary containing the configuration parameters for the database connection.
    """
    def __init__(self, name: Text, connection_data: Dict):
        self.name = name
        self.connection_data = connection_data
        self.connection = self.create_connection()
        self.inspector = self.create_inspector()

    @abstractmethod
    def create_connection(self) -> Any:
        """
        Create a connection to a database.
        :return: A SQLAlchemy engine object or a similar connection object for establishing a connection to a database.
        """
        raise NotImplementedError

    def get_connector_name(self) -> Text:
        """
        Get the name of the connector.
        :return: The name of the connector.
        """
        return self.name

    def create_inspector(self) -> sqlalchemy.Inspector:
        """
        Create an SQLAlchemy inspector object for the connection to the database.
        :return: An SQLAlchemy inspector object.
        """
        return inspect(self.connection)

    def get_tables(self) -> List[Text]:
        """
        Get the tables of the database.
        This method must be implemented by subclasses if the database does not support the inspector.
        :return: The tables of the database.
        """
        return self.inspector.get_table_names()

    def get_columns(self, table_name) -> List[Text]:
        """
        Get the columns of a table.
        This method must be implemented by subclasses if the database does not support the inspector.
        :param table_name: The name of the table.
        :return: The columns of the table.
        """
        return [column['name'] for column in self.inspector.get_columns(table_name)]

    def query(self, query: Text) -> List[Dict]:
        """
        Execute a query on the database.
        This method must be implemented by subclasses if the given implementation is not sufficient.
        :param query: The query to execute.
        :return: The result of the query.
        """
        with self.connection.connect() as conn:
            result = conn.execute(text(query))
        return result.fetchall()
