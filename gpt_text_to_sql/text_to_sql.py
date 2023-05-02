import os
import openai
import pandas as pd
from .gpt import GPT
from typing import Optional, Text, Dict


class TextToSQL:
    def __init__(self, connector_name: Text, connection_data: Optional[Dict], api_key: Optional[Text] = None):
        self.gpt = GPT(connector_name, connection_data)
        self._set_openai_api_key(api_key)

    def convert_text_to_sql(self, text: Text):
        return self.gpt.get_top_reply(text).strip()

    def query(self, query: Text):
        sql = self.convert_text_to_sql(query)
        return self.gpt.connector.query(sql)

    def query_df(self, query: Text):
        sql = self.convert_text_to_sql(query)
        return pd.DataFrame(self.gpt.connector.query(sql))

    def _set_openai_api_key(self, api_key):
        api_key = api_key or os.getenv('OPENAI_API_KEY')
        if api_key is not None:
            openai.api_key = api_key
        else:
            raise Exception("No OpenAI API key provided. Please provide an API key or set the OPENAI_API_KEY environment variable.")

