import os
from typing import TYPE_CHECKING, Dict, List, Text, Union

from openai import OpenAI

if TYPE_CHECKING:
    from langchain_openai import ChatOpenAI


from ai_text_to_sql.exceptions import NoOpenAIAPIKeyException
from ai_text_to_sql.llm_connectors.llm_connector import LLMConnector


class OpenAIConnector(LLMConnector):
    """
    The class for interacting with the OpenAI API.

    Parameters
    ----------
    api_key: Text
        The API key for the OpenAI API. This parameter is optional, but if not provided,
        the OPENAI_API_KEY environment variable must be set.
    engine: Text
        The engine to use for the OpenAI API. This parameter is optional, and defaults
        to "text-davinci-003".
    temperature: float
        The temperature for the OpenAI API. This parameter is optional, and defaults to
        0.
    max_tokens: int
        The maximum number of tokens for the OpenAI API. This parameter is optional,
        and defaults to 150.
    top_p: float
        The top p for the OpenAI API. This parameter is optional, and defaults to 1.0.
    frequency_penalty: float
        The frequency penalty for the OpenAI API. This parameter is optional, and
        defaults to 0.0.
    presence_penalty: float
        The presence penalty for the OpenAI API. This parameter is optional, and
        defaults to 0.0.
    stop: List[Text]
        The stop for the OpenAI API. This parameter is optional, and defaults to
        ("#", ";").
    """

    name = "OpenAI"

    def __init__(
        self,
        api_key: Union[Text, None] = None,
        model: Text = "gpt-3.5-turbo",
        temperature: int = 0,
        max_tokens: int = 150,
        top_p: float = 1.0,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0,
        stop: tuple = ("#", ";"),
    ) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY") or None
        if self.api_key is None:
            raise NoOpenAIAPIKeyException(
                "No OpenAI API key provided. Please provide an API key or set the "
                "OPENAI_API_KEY environment variable."
            )

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.stop = list(stop)

        self.client = OpenAI(
            api_key=self.api_key,
        )

    def get_answer(
        self, prompt: Union[Text, None] = None, messages: Union[List[Dict], None] = None
    ) -> Text:
        """
        Calls the OpenAI Completion API with the provided prompt.
        :param prompt: The prompt for the API call.
        :return: The response (SQL query) from the API call.
        """
        if not prompt and not messages:
            raise ValueError("Either prompt or messages must be provided.")

        if prompt and messages:
            raise ValueError("Only one of prompt or messages can be provided.")

        if prompt:
            messages = [{"role": "user", "content": prompt}]

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            stop=self.stop,
            messages=messages,  # type: ignore[arg-type]
        )

        return response.choices[0].message.content or ""

    def create_prompt(
        self, user_input: Text, database_schema: Dict, connector_name: Text
    ) -> Text:
        """
        Creates the prompt for the API call by incorporating the user input and the
        database schema.
        :param user_input: The user input to be converted to SQL.
        :param database_schema: The database schema to use for the prompt as a
                                formatted string.
        :param connector_name: The name of the connector.
        :return: The prompt for the API call.
        """
        return (
            self.format_database_schema(database_schema, connector_name)
            + "\n"
            + user_input
            + "\nYour response should be a clear and concise SQL statement that"
            " retrieves only the necessary data from the relevant tables. "
            "Please ensure that your query is optimized for performance and "
            "accuracy. Your response should only include the SQL statement,"
            " without any additional text or enclosing characters."
        )

    def format_database_schema(
        self, database_schema: Dict, connector_name: Text
    ) -> Text:
        """
        Formats the database schema for the prompt.
        :param database_schema: The database schema to format.
        :param connector_name: The name of the connector.
        :return: A formatted string containing the database schema.
        """
        formatted_database_schema = (
            f"### {connector_name} tables, with their properties:\n#\n"
        )
        formatted_database_schema += "\n".join(
            [
                f"# {table_name} ({', '.join(columns)})"
                for table_name, columns in database_schema.items()
            ]
        )

        return formatted_database_schema

    def to_langchain(self) -> "ChatOpenAI":
        """
        Converts the OpenAI connector to a LangChain ChatOpenAI model.
        :return: The LangChain chat model.
        """
        try:
            from langchain_openai import ChatOpenAI

            return ChatOpenAI(
                api_key=self.api_key,
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
                stop=self.stop,
            )
        except ImportError:
            raise ImportError(
                "The langchain-openai package is required to use this connector with "
                "the agent. "
                "Please run 'pip install langchain-openai' to install it."
            )
