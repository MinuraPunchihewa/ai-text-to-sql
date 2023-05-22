import os
import openai
from typing import Text, Dict, List

import logging
import logging.config

from ai_text_to_sql.llms.llm import LLM
from ai_text_to_sql.config_parser import ConfigParser
from ai_text_to_sql.connectors.connector import Connector

logging_config_parser = ConfigParser()
logging.config.dictConfig(logging_config_parser.get_config_dict())
logger = logging.getLogger()


class OpenAILLM(LLM):
    """
    The class for interacting with the OpenAI API.

    Parameters
    ----------
    api_key: Text
        The API key for the OpenAI API.
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
    name = 'OpenAI'

    def __init__(self,
                 api_key=None,
                 engine='text-davinci-003',
                 temperature=0,
                 max_tokens=150,
                 top_p=1.0,
                 frequency_penalty=0.0,
                 presence_penalty=0.0,
                 stop=("#", ";")):
        super().__init__(api_key)
        self.set_api_key()

        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.stop = list(stop)

        self.logger = logger

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

    def get_prime_text(self, connector: Connector) -> Text:
        """
        Get the prime text for the request to the OpenAI API using the Database Connector (tables and their columns).
        :param connector: The DatabaseConnector object to use.
        :return: A string containing all examples formatted for the API.
        """
        prime_text = f"### {connector.get_connector_name()} tables, with their properties:\n#\n"
        tables = connector.get_tables()
        for table in tables:
            columns = connector.get_columns(table)
            prime_text += f"# {table}(" + ", ".join(columns) + ")\n"

        return prime_text

    def craft_prompt(self, text: Text, prime_text: Text) -> Text:
        """
        Creates the query for the API request.
        :param text: The text provided by the user.
        :param prime_text: The prime text to use for the API request.
        :return: The query for the API request.
        """
        return prime_text + text + "\nYour response should be a clear and concise SQL statement that" \
                                   " retrieves only the necessary data from the relevant tables. " \
                                   "Please ensure that your query is optimized for performance and " \
                                   "accuracy. Your response should only include the SQL statement," \
                                   " without any additional text."

    def submit_request(self, prompt: Text) -> Dict:
        """
        Calls the OpenAI API with the crafted prompt.
        :param prompt: The prompt to query the API with.
        :return: The API response.
        """
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

    def get_top_reply(self, text: Text, connector: Connector) -> Text:
        """
        Obtains the best result as returned by the API.
        :param text: The text provided by the user.
        :param connector: The DatabaseConnector object to use.
        :return: The best result returned by the API.
        """
        prime_text = self.get_prime_text(connector)
        prompt = self.craft_prompt(text, prime_text)
        self.logger.info(f"Prompt: {prompt}")

        response = self.submit_request(prompt)
        return response['choices'][0]['text']

    def set_api_key(self):
        """
        Set the OpenAI API key.
        :return: None.
        """
        api_key = self.api_key or os.getenv('OPENAI_API_KEY')
        if self.api_key is not None:
            openai.api_key = api_key
        else:
            raise Exception(
                "No OpenAI API key provided. Please provide an API key or set the OPENAI_API_KEY environment variable."
            )
