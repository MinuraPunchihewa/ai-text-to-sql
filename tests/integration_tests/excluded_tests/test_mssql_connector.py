import os
import unittest
from typing import ClassVar

from dotenv import load_dotenv

from ai_text_to_sql import TextToSQL
from ai_text_to_sql.data_connectors.mssql_connector import MSSQLConnector
from ai_text_to_sql.llm_connectors.openai_connector import OpenAIConnector

load_dotenv()


class TestMSSQLConnector(unittest.TestCase):
    tts: ClassVar[TextToSQL]

    @classmethod
    def setUpClass(cls) -> None:
        mssql_connector = MSSQLConnector(
            user=os.environ.get("MSSQL_USER"),
            port=int(os.environ.get("MSSQL_PORT", "1433")),
            password=os.environ.get("MSSQL_PASSWORD"),
            host=os.environ.get("MSSQL_HOST"),
            database=os.environ.get("MSSQL_DATABASE"),
            schema=os.environ.get("MSSQL_SCHEMA"),
        )

        openai_connector = OpenAIConnector(api_key=os.environ.get("OPENAI_API_KEY"))
        cls.tts = TextToSQL(mssql_connector, openai_connector)

    def test_convert_text_to_sql(self) -> None:
        self.assertEqual(
            self.tts.convert_text_to_sql(
                "Get me list of people whose last name is Torres."
            ),
            "SELECT * FROM person WHERE last_name = 'Torres'",
        )
