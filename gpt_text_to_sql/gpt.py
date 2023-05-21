import openai
from typing import Text, Dict, List

import logging
import logging.config

from .config_parser import ConfigParser
from gpt_text_to_sql.connectors.database_connector_factory import DatabaseConnectorFactory

logging_config_parser = ConfigParser()
logging.config.dictConfig(logging_config_parser.get_config_dict())
logger = logging.getLogger()


class GPT:
    """
    The class for interacting with the OpenAI API.

    Parameters
    ----------
    connector_name: Text
        The name of the connector.
    connection_data: Dict
        A dictionary containing the configuration parameters for the database connection.
    engine: Text
        The engine to use for the OpenAI API.
    temperature: float
        The temperature for the OpenAI API.
    max_tokens: int
        The maximum number of tokens for the OpenAI API.
    top_p: float
        The top p for the OpenAI API.
    frequency_penalty: float
        The frequency penalty for the OpenAI API.
    presence_penalty: float
        The presence penalty for the OpenAI API.
    stop: List[Text]
        The stop for the OpenAI API.
    """
    def __init__(self,
                 connector_name,
                 connection_data,
                 engine='text-davinci-003',
                 temperature=0,
                 max_tokens=150,
                 top_p=1.0,
                 frequency_penalty=0.0,
                 presence_penalty=0.0,
                 stop=("#", ";")):
        self.connector = DatabaseConnectorFactory.build_connector(connector_name, connection_data)
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.stop = list(stop)

        self.logger = logger

    def get_prime_text(self) -> Text:
        """
        Formats all examples to prime the model.
        :return: A string containing all examples formatted for the API.
        """
        prime_text = f"{self.connector.name} tables, with their properties:\n#\n"
        tables = self.connector.get_tables()
        for table in tables:
            columns = self.connector.get_columns(table)
            prime_text += f"# {table}(" + ", ".join(columns) + ")\n"

        prime_text += "#\n### "
        return prime_text

    def get_engine(self) -> Text:
        """
        Returns the engine specified for the API.
        :return: The engine specified for the API.
        """
        return self.engine

    def get_temperature(self) -> float:
        """
        Returns the temperature specified for the API.
        :return: The temperature specified for the API.
        """
        return self.temperature

    def get_top_p(self) -> float:
        """
        Returns the top_p specified for the API.
        :return: The top_p specified for the API.
        """
        return self.top_p

    def get_frequency_penalty(self) -> float:
        """
        Returns the frequency_penalty specified for the API.
        :return: The frequency_penalty specified for the API.
        """
        return self.frequency_penalty

    def get_presence_penalty(self) -> float:
        """
        Returns the presence_penalty specified for the API.
        :return: The presence_penalty specified for the API.
        """
        return self.presence_penalty

    def get_max_tokens(self) -> int:
        """
        Returns the max tokens specified for the API.
        :return: The max tokens specified for the API.
        """
        return self.max_tokens

    def craft_query(self, prompt) -> Text:
        """
        Creates the query for the API request.
        :param prompt: The prompt to query the API with.
        :return: The query for the API request.
        """
        return self.get_prime_text() + prompt

    def submit_request(self, prompt) -> Dict:
        """
        Calls the OpenAI API with the specified parameters.
        :param prompt: The prompt to query the API with.
        :return: The API response.
        """
        prompt = self.craft_query(prompt)
        self.logger.info(f"Modified prompt: {prompt}")

        response = openai.Completion.create(engine=self.get_engine(),
                                            prompt=prompt,
                                            max_tokens=self.get_max_tokens(),
                                            temperature=self.get_temperature(),
                                            top_p=self.get_top_p(),
                                            frequency_penalty=self.get_frequency_penalty(),
                                            presence_penalty=self.get_presence_penalty(),
                                            stream=False,
                                            stop=self.stop)
        return response

    def get_top_reply(self, prompt) -> Text:
        """
        Obtains the best result as returned by the API.
        :param prompt: The prompt to query the API with.
        :return: The best result returned by the API.
        """
        response = self.submit_request(prompt)
        return response['choices'][0]['text']
