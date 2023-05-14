import os
import openai
import pandas as pd
from .gpt import GPT
from typing import Optional, Text, List, Dict

import logging
import logging.config
from .config_parser import ConfigParser

logging_config_parser = ConfigParser()
logging.config.dictConfig(logging_config_parser.get_config_dict())
logger = logging.getLogger()


class TextToSQL:
    """
    The class for converting text to SQL query and querying the database.

    Parameters:
    -----------
    connector_name: Text
        The name of the connector.
    connection_data: Dict
        A dictionary containing the configuration parameters for the database connection.
    """
    def __init__(self, connector_name: Text, connection_data: Optional[Dict], api_key: Optional[Text] = None):
        self.gpt = GPT(connector_name, connection_data)
        self._set_openai_api_key(api_key)

        self.logger = logger

    def convert_text_to_sql(self, text: Text) -> Text:
        """
        Convert text to SQL query.
        :param text: The Text to convert to SQL query.
        :return: The converted SQL query.
        """
        sql = self.gpt.get_top_reply(text).strip()
        self.logger.info(f"SQL query: {sql}")
        return sql

    def query(self, text: Text) -> List[Dict]:
        """
        Query the database.
        :param text: The text to convert to SQL query and query the database.
        :return: The query result.
        """
        sql = self.convert_text_to_sql(text)
        return self.gpt.connector.query(sql)

    def query_df(self, text: Text) -> pd.DataFrame:
        """
        Query the database and return the result as a Pandas DataFrame.
        :param text: The text to convert to SQL query and query the database.
        :return: A Pandas DataFrame containing the query result.
        """
        sql = self.convert_text_to_sql(text)
        return pd.DataFrame(self.gpt.connector.query(sql))

    def _set_openai_api_key(self, api_key):
        """
        Set the OpenAI API key.
        :param api_key: A valid OpenAI API key.
        :return: None.
        """
        api_key = api_key or os.getenv('OPENAI_API_KEY')
        if api_key is not None:
            openai.api_key = api_key
        else:
            raise Exception("No OpenAI API key provided. Please provide an API key or set the OPENAI_API_KEY environment variable.")

