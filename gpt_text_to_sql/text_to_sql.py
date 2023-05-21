import pandas as pd
from typing import Optional, Text, List, Dict

import logging.config

from .config_parser import ConfigParser
from .llms.llm_factory import LLMFactory
from .connectors.database_connector_factory import DatabaseConnectorFactory

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
    def __init__(self, connector_name: Text, connection_data: Optional[Dict], llm_name: Text, api_key: Optional[Text] = None):
        self.llm = LLMFactory.build_llm(llm_name, api_key)
        self.connector = DatabaseConnectorFactory.build_connector(connector_name, connection_data)

        self.logger = logger

    def convert_text_to_sql(self, text: Text) -> Text:
        """
        Convert text to SQL query.
        :param text: The Text to convert to SQL query.
        :return: The converted SQL query.
        """
        sql = self.llm.get_top_reply(text, self.connector).strip()
        self.logger.info(f"SQL query: {sql}")
        return sql

    def query(self, text: Text) -> List[Dict]:
        """
        Query the database.
        :param text: The text to convert to SQL query and query the database.
        :return: The query result.
        """
        sql = self.convert_text_to_sql(text)
        return self.connector.query(sql)

    def query_df(self, text: Text) -> pd.DataFrame:
        """
        Query the database and return the result as a Pandas DataFrame.
        :param text: The text to convert to SQL query and query the database.
        :return: A Pandas DataFrame containing the query result.
        """
        sql = self.convert_text_to_sql(text)
        return pd.DataFrame(self.gpt.connector.query(sql))

