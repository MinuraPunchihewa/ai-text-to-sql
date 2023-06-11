from abc import ABC, abstractmethod
from typing import Text, Dict


class LLM(ABC):
    """
    The abstract base class for LLMs.
    """

    @abstractmethod
    def format_database_schema(self, database_schema: Dict, connector_name: Text) -> Text:
        """
        Formats the database schema for the prompt.
        The database schema is a dictionary containing the tables and columns of the database.
        E.g.: {"table1": ["column1", "column2"], "table2": ["column1", "column2"]}
        :param database_schema: The database schema to format.
        :param connector_name: The name of the connector.
        :return: A formatted string containing the database schema.
        """
        raise NotImplementedError

    @abstractmethod
    def create_prompt(self, user_input: Text, database_schema: Text, connector_name: Text) -> Text:
        """
        Creates the prompt for the API call by incorporating the user input and the database schema.
        Use the format_database_schema method to format the database schema as required and incorporate it into the prompt.
        :param user_input: The user input to be converted to SQL.
        :param database_schema: The database schema to use for the prompt as a formatted string.
        :param connector_name: The name of the connector.
        :return: The prompt for the API call.
        """
        raise NotImplementedError

    @abstractmethod
    def get_answer(self, prompt: Text) -> Text:
        """
        Calls the LLM and returns the response.
        :param prompt: The prompt for the API call.
        :return: The response (SQL query) from the API call.
        """
        raise NotImplementedError
