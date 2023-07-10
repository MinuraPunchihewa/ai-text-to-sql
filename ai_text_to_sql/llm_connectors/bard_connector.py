from typing import Text, Dict

from ai_text_to_sql.llm_connectors.llm_connector import LLMConnector


class BardConnector(LLMConnector):
    name = 'Bard'

    def format_database_schema(self, database_schema: Dict, connector_name: Text) -> Text:
        pass

    def create_prompt(self, user_input: Text, database_schema: Dict, connector_name: Text) -> Text:
        pass

    def get_answer(self, prompt: Text) -> Text:
        pass
