from abc import ABC, abstractmethod
from typing import Text, Dict


class LLMConnector(ABC):
    """
    The abstract base class for LLMs.

    To add a new LLM connector, follow these steps:
    1. Create a new module in the llm_connectors directory.
    2. Create a new class in the module that inherits from the base LLMConnector class.
    3. Add the 'name' attribute to the new class to set the name of the connector.
    4. Implement the format_database_schema(), create_prompt() and get_answer() abstract methods.
    5. Add an import statement for the new class in the __init__.py file in the llm_connectors directory.
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
    def create_prompt(self, user_input: Text, database_schema: Dict, connector_name: Text) -> Text:
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
