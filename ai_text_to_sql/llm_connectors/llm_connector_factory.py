import sys
import inspect
from typing import Dict, Type, Text

from .llm_connector import LLMConnector
from ai_text_to_sql.llm_connectors import *

from ai_text_to_sql.exceptions import UnsupportedLLMConnectorException


class LLMConnectorFactory:
    """
    The class for building LLMs.
    """
    @staticmethod
    def build_llm(name: Text, **kwargs) -> LLMConnector:
        """
        Build a LLM.
        :param name: The name of the LLM.
        :param kwargs: The parameters for the LLM.
        :return: A LLM.
        """
        llms = LLMConnectorFactory._discover_llms()
        if name in llms:
            return llms[name](**kwargs)
        else:
            raise UnsupportedLLMConnectorException(f"Unsupported LLM: {name}")

    @staticmethod
    def _discover_llms() -> Dict[str, Type[LLMConnector]]:
        """
        Discover available LLMs dynamically.
        :return: A dictionary mapping LLM names to their corresponding classes.
        """
        llms = {}
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj) and issubclass(obj, LLMConnector) and obj is not LLMConnector:
                llms[obj.__name__[:-9]] = obj  # Remove "Connector" from class name
        return llms
