import pandas as pd
from .gpt import GPT
from typing import Optional, Text, Dict


class TextToSQL:
    def __init__(self, connector_name: Text, connection_data: Optional[Dict]):
        self.gpt = GPT(connector_name, connection_data)

    def convert_text_to_sql(self, text: Text):
        return self.gpt.get_top_reply(text)

    def query(self, query: Text):
        sql = self.convert_text_to_sql(query)
        return self.gpt.connector.query(sql)

    def query_df(self, query: Text):
        sql = self.convert_text_to_sql(query)
        return pd.DataFrame(self.gpt.connector.query(sql))
