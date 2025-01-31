from typing import Dict, List, Text

from .llm_connectors.llm_connector import LLMConnector
from .data_connectors.data_connector import DataConnector


class TextToSQLAgent:
    """
    The class for invoking an agent against the configured database.

    Parameters:
    -----------
    llm_connector : LLMConnector
        The LLMConnector to use for converting text to SQL query.
    data_connector : DataConnector
        The DataConnector to use for querying the database.
    """
    def __init__(self, data_connector: DataConnector, llm_connector: LLMConnector):
        try:
            from langchain_community.utilities.sql_database import SQLDatabase
            from langchain_community.agent_toolkits import create_sql_agent

            db = SQLDatabase.from_uri(
                data_connector.get_connection_string()
            )
            llm = llm_connector.to_langchain()

            self.agent_executor = create_sql_agent(llm, db=db, verbose=True)
        except ImportError:
            raise ImportError("The langchain-community package is required to use the agent.")

    def query(self, text: Text) -> List[Dict]:
        """
        Query/invoke the agaent.
        :param text: The text to invoke the agent with.
        :return: The response from the agent.
        """
        response = self.agent_executor.invoke(text)
        return response["output"]
    