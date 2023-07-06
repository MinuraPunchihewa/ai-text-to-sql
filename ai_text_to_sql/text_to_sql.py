import pandas as pd
from typing import Optional, Text, List, Dict

import logging.config

from .config_parser import ConfigParser
from .llm_connectors.llm_connector import LLMConnector
from .data_connectors.data_connector import DataConnector

logging_config_parser = ConfigParser()
logging.config.dictConfig(logging_config_parser.get_config_dict())
logger = logging.getLogger()


class TextToSQL:
    """
    The class for converting text to SQL query and querying the database.

    Parameters:
    -----------
    llm_connector : LLMConnector
        The LLMConnector to use for converting text to SQL query.
    data_connector : DataConnector
        The DataConnector to use for querying the database.
    """
    def __init__(self, data_connector: DataConnector, llm_connector: LLMConnector):
        self.data_connector = data_connector
        self.llm_connector = llm_connector

        self.logger = logger

    def convert_text_to_sql(self, text: Text) -> Text:
        """
        Convert text to SQL query.
        :param text: The Text to convert to SQL query.
        :return: The converted SQL query.
        """
        prompt = self.llm_connector.create_prompt(
            text,
            self.data_connector.get_database_schema(),
            self.data_connector.get_connector_name()
        )
        self.logger.info(f"Prompt: {prompt}")

        sql = self.llm_connector.get_answer(prompt).strip()
        self.logger.info(f"SQL query: {sql}")
        return sql

    def query(self, text: Text) -> List[Dict]:
        """
        Query the database.
        :param text: The text to convert to SQL query and query the database.
        :return: The query result.
        """
        sql = self.convert_text_to_sql(text)
        return self.data_connector.query(sql)

    def query_df(self, text: Text) -> pd.DataFrame:
        """
        Query the database and return the result as a Pandas DataFrame.
        :param text: The text to convert to SQL query and query the database.
        :return: A Pandas DataFrame containing the query result.
        """
        sql = self.convert_text_to_sql(text)
        return pd.DataFrame(self.data_connector.query(sql))

