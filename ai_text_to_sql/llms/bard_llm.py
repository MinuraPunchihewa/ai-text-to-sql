from typing import Text

from ai_text_to_sql.llms.llm import LLM


class Bard(LLM):
    def create_prompt(self, user_input: Text, database_schema: Text) -> Text:
        pass

    def get_answer(self, prompt: Text) -> Text:
        pass