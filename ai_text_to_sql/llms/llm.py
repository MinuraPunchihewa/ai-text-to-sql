from abc import ABC, abstractmethod
from typing import Text


class LLM(ABC):
    """
    The abstract base class for LLMs.
    """

    @abstractmethod
    def create_prompt(self, user_input: Text, database_schema: Text) -> Text:
        """
        Creates the prompt for the API call by incorporating the user input and the database schema.
        :param user_input: The user input to be converted to SQL.
        :param database_schema: The database schema to use for the prompt as a formatted string.
        :return: The prompt for the API call.
        """
        raise NotImplementedError

    @abstractmethod
    def get_answer(self, prompt: Text) -> Text:
        """
        Calls the LLM's API and returns the response.
        :param prompt: The prompt for the API call.
        :return: The response (SQL query) from the API call.
        """
        raise NotImplementedError
