import sys
import inspect
from typing import Optional, Dict, Type, Text

from .llm import LLM
from ai_text_to_sql.llms import *


class LLMFactory:
    """
    The class for building LLMs.
    """
    @staticmethod
    def build_llm(name: Text, api_key: Text, **kwargs) -> LLM:
        """
        Build a LLM.
        :param name: The name of the LLM.
        :param api_key: The API key for the LLM.
        :return: A LLM.
        """
        llms = LLMFactory._discover_llms()
        if name in llms:
            return llms[name](api_key, **kwargs)
        else:
            raise ValueError(f"Unsupported LLM: {name}")

    @staticmethod
    def _discover_llms() -> Dict[str, Type[LLM]]:
        """
        Discover available LLMs dynamically.
        :return: A dictionary mapping LLM names to their corresponding classes.
        """
        llms = {}
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj) and issubclass(obj, LLM) and obj is not LLM:
                llms[obj.__name__[:-3]] = obj  # Remove "LLM" from class name
        return llms
