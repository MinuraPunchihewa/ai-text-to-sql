import os
from bardapi import Bard as BardAPI
from typing import Text, Dict

import logging
import logging.config

from ai_text_to_sql.llms.llm import BaseAPILLM
from ai_text_to_sql.config_parser import ConfigParser
from ai_text_to_sql.connectors.connector import Connector

logging_config_parser = ConfigParser()
logging.config.dictConfig(logging_config_parser.get_config_dict())
logger = logging.getLogger()


class Bard(BaseAPILLM):
    def __init__(self, api_key=None):
        super().__init__(api_key)
        self.bard = self.set_api_key()

        self.logger = logger

    def get_prime_text(self, connector: Connector):
        """
        Get the prime text for the request to the Bard API using the Database Connector (tables and their columns).
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
        Calls the Bard API with the crafted prompt.
        :param prompt: The prompt to query the API with.
        :return: The API response.
        """
        response = self.bard.get_answer(prompt)

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
        return response['textQuery'][0]

    def set_api_key(self) -> BardAPI:
        """
        Sets the Bard API key.
        :return: The Bard object.
        """
        api_key = self.api_key or os.getenv('BARD_API_KEY')
        if api_key is not None:
            return BardAPI(token=api_key)
        else:
            raise Exception(
                "No Bard API key provided. Please provide an API key or set the BARD_API_KEY environment variable."
            )
