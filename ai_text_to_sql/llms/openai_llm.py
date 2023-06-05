import os
import openai
from typing import Text, List

from ai_text_to_sql.llms.llm import LLM


class OpenAI(LLM):
    """
    The class for interacting with the OpenAI API.

    Parameters
    ----------
    api_key: Text
        The API key for the OpenAI API.
    engine: Text
        The engine to use for the OpenAI API.
    temperature: float
        The temperature for the OpenAI API.
    max_tokens: int
        The maximum number of tokens for the OpenAI API.
    top_p: float
        The top p for the OpenAI API.
    frequency_penalty: float
        The frequency penalty for the OpenAI API.
    presence_penalty: float
        The presence penalty for the OpenAI API.
    stop: List[Text]
        The stop for the OpenAI API.
    """
    name = 'OpenAI'

    def __init__(self,
                 api_key=None,
                 engine="text-davinci-003",
                 temperature=0,
                 max_tokens=150,
                 top_p=1.0,
                 frequency_penalty=0.0,
                 presence_penalty=0.0,
                 stop=("#", ";")):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY") or None
        if self.api_key is None:
            raise Exception(
                "No OpenAI API key provided. Please provide an API key or set the OPENAI_API_KEY environment variable."
            )
        openai.api_key = self.api_key

        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.stop = list(stop)

        self.context = []

    def get_engine(self) -> Text:
        """
        Returns the engine specified for the API.
        :return: The engine specified for the API.
        """
        return self.engine

    def get_temperature(self) -> float:
        """
        Returns the temperature specified for the API.
        :return: The temperature specified for the API.
        """
        return self.temperature

    def get_top_p(self) -> float:
        """
        Returns the top_p specified for the API.
        :return: The top_p specified for the API.
        """
        return self.top_p

    def get_frequency_penalty(self) -> float:
        """
        Returns the frequency_penalty specified for the API.
        :return: The frequency_penalty specified for the API.
        """
        return self.frequency_penalty

    def get_presence_penalty(self) -> float:
        """
        Returns the presence_penalty specified for the API.
        :return: The presence_penalty specified for the API.
        """
        return self.presence_penalty

    def get_max_tokens(self) -> int:
        """
        Returns the max tokens specified for the API.
        :return: The max tokens specified for the API.
        """
        return self.max_tokens

    def get_answer(self, prompt: Text) -> Text:
        """
        Calls the OpenAI Completion API with the provided prompt.
        :param prompt: The prompt for the API call.
        :return: The response (SQL query) from the API call.
        """
        response = openai.Completion.create(engine=self.get_engine(),
                                            prompt=prompt,
                                            max_tokens=self.get_max_tokens(),
                                            temperature=self.get_temperature(),
                                            top_p=self.get_top_p(),
                                            frequency_penalty=self.get_frequency_penalty(),
                                            presence_penalty=self.get_presence_penalty(),
                                            stream=False,
                                            stop=self.stop)

        return response["choices"][0]["text"]

    def create_prompt(self, user_input: Text, database_schema: Text) -> Text:
        """
        Creates the prompt for the API call by incorporating the user input and the database schema.
        :param user_input: The user input to be converted to SQL.
        :param database_schema: The database schema to use for the prompt as a formatted string.
        :return: The prompt for the API call.
        """
        prompt = "Your task is to convert natural language commands into SQL queries.\nYou will be given a " \
                 "database schema and natural language commands. Your response should be clear and concise SQL " \
                 "statements that retrieve or modify data from the relevant tables. Please ensure that your queries " \
                 "are optimized for performance and accuracy. Your response should only include the SQL statement, " \
                 "without any additional text.\nThe database schema will be delimited by triple hashtags and " \
                 "individual tables will be delimited by single hashtags.\n\n"

        prompt += database_schema + "\nThe natural language command:\n```" + user_input + "```\n"

        return prompt
