from typing import Text

from ai_text_to_sql.llm_connectors.llm_connector import LLMConnector


class Bard(LLMConnector):
    def create_prompt(self, user_input: Text, database_schema: Text) -> Text:
        pass

    def get_answer(self, prompt: Text) -> Text:
        pass