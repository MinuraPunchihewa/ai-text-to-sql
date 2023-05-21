from abc import ABC, abstractmethod
from typing import Text, Dict, List, Any

from gpt_text_to_sql.connectors.database_connector import DatabaseConnector


class LLM(ABC):
    """
    The abstract base class for LLMs.

    Parameters
    ----------
    api_key: Text
        The API key for the LLM.
    """
    def __init__(self, api_key: Text):
        self.api_key = api_key

    @abstractmethod
    def get_prime_text(self, connector: DatabaseConnector):
        """
        Get the prime text for the request to the LLM using the Database Connector.
        :param connector: The database connector.
        """
        raise NotImplementedError

    @abstractmethod
    def craft_prompt(self, connector: DatabaseConnector) -> Text:
        """
        Craft the prompt for the request to the LLM using the prime text and any additional text.
        :param connector: The database connector.
        :return: The prompt for the request to the LLM.
        """
        raise NotImplementedError

    @abstractmethod
    def submit_request(self, prompt: Text) -> Dict:
        """
        Submit a request to the LLM using the crafted prompt.
        :param prompt: The prompt for the request to the LLM.
        :return: The response from the LLM.
        """
        raise NotImplementedError

    @abstractmethod
    def get_top_reply(self) -> Text:
        """
        Get the top reply from the LLM.
        :return: The top reply from the LLM.
        """
        raise NotImplementedError

    @abstractmethod
    def set_api_key(self, api_key: Text):
        """
        Set the API key for the LLM.
        :param api_key: The API key for the LLM.
        """
        raise NotImplementedError
