import logging.config
from typing import Text

from .config_parser import ConfigParser
from .data_connectors.data_connector import DataConnector
from .llm_connectors.llm_connector import LLMConnector
from .text_to_sql import TextToSQL

logging_config_parser = ConfigParser()
logging.config.dictConfig(logging_config_parser.get_config_dict())
logger = logging.getLogger()


class TextToSQLChatMemory:
    def __init__(self):
        self.memory = []

    def add(self, role: Text, content: Text):
        self.memory.append(
            {
                "role": role,
                "content": content,
                
            }
        )

    def get(self):
        return self.memory


class TextToSQLChat(TextToSQL):
    def __init__(self, data_connector: DataConnector, llm_connector: LLMConnector):
        super().__init__(data_connector, llm_connector)
        self.memory = TextToSQLChatMemory()

        # Add the system prompt to the memory.
        system_prompt = self.llm_connector.create_prompt(
            "",
            self.data_connector.get_database_schema(),
            self.data_connector.get_connector_name(),
        )
        self.logger.info(f"System prompt: {system_prompt}")

        self.memory.add(
            "system",
            system_prompt
        )
        
    def convert_text_to_sql(self, text: Text) -> Text:
        """
        Convert text to SQL query.
        :param text: The Text to convert to SQL query.
        :return: The converted SQL query.
        """
        pass

