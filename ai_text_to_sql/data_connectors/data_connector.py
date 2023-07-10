from abc import ABC, abstractmethod
from typing import Text, Dict, List, Any

import sqlalchemy
from sqlalchemy import inspect, text


class DataConnector(ABC):
    """
    The abstract base class for database connectors.

    To add a new data connector, follow these steps:
    1. Create a new module in the data_connectors directory.
    2. Create a new class in the module that inherits from the base DataConnector class.
    3. Add the 'name' attribute to the new class to set the name of the connector.
    4. Implement the create_connection() abstract method.
    5. Implement the get_tables() and get_columns() methods if the database does not support SQLAlchemy Inspector.
    6. Add an import statement for the new class in the __init__.py file in the data_connectors directory.
    """
    name = "Base"

    def __init__(self):
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

    def get_database_schema(self) -> Dict:
        """
        Get the database schema as a dictionary.
        :return: A dictionary containing the database schema.
        """
        database_schema = {}
        tables = self.get_tables()
        for table in tables:
            columns = self.get_columns(table)
            database_schema[table] = columns

        return database_schema

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
