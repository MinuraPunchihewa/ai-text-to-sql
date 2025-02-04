import logging.config
from typing import Text, Union

from .config_parser import ConfigParser
from .data_connectors.data_connector import DataConnector
from .llm_connectors.llm_connector import LLMConnector
from .text_to_sql import TextToSQL

logging_config_parser = ConfigParser()
logging.config.dictConfig(logging_config_parser.get_config_dict())
logger = logging.getLogger()


class TextToSQLChatMemory:
    def __init__(self, system_prompt: Text, window_size: Union[int, None] = None):
        self.system_prompt = system_prompt
        self.window_size = window_size
        self.memory = []

    def add_message(self, role: Text, content: Text):
        self.memory.append(
            {
                "role": role,
                "content": content,
                
            }
        )

    def get_messages(self):
        if self.window_size is None or len(self.memory) <= self.window_size:
            return [{"role": "system", "content": self.system_prompt}] + self.memory
        else:
            # Return the last 'window_size' elements of the memory.
            return (
                [{"role": "system", "content": self.system_prompt}] +
                self.memory[-self.window_size:]
            )


class TextToSQLChat(TextToSQL):
    def __init__(
            self,
            data_connector: DataConnector,
            llm_connector: LLMConnector,
            window_size: Union[int, None] = None
        ):
        super().__init__(data_connector, llm_connector)

        # Add the system prompt to the memory.
        system_prompt = self.llm_connector.create_prompt(
            "",
            self.data_connector.get_database_schema(),
            self.data_connector.get_connector_name(),
        )
        self.logger.info(f"System prompt: {system_prompt}")

        self.memory = TextToSQLChatMemory(system_prompt, window_size=window_size)
        
    def convert_text_to_sql(self, text: Text) -> Text:
        """
        Convert text to SQL query.
        :param text: The Text to convert to SQL query.
        :return: The converted SQL query.
        """
        self.memory.add_message(
            "user",
            text
        )

        sql = self.llm_connector.get_answer(
            messages=self.memory.get_messages()
        ).strip()
        self.logger.info(f"SQL query: {sql}")

        self.memory.add_message(
            "system",
            sql
        )

        return sql

