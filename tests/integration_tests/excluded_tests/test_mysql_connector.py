import os
import unittest
from typing import ClassVar

from dotenv import load_dotenv

from ai_text_to_sql import TextToSQL
from ai_text_to_sql.data_connectors.mysql_connector import MySQLConnector
from ai_text_to_sql.llm_connectors.openai_connector import OpenAIConnector

load_dotenv()


class TestMySQLConnector(unittest.TestCase):
    tts: ClassVar[TextToSQL]

    @classmethod
    def setUpClass(cls) -> None:
        mysql_connector = MySQLConnector(
            user=os.environ.get("MYSQL_USER"),
            port=int(os.environ.get("MYSQL_PORT")),
            password=os.environ.get("MYSQL_PASSWORD"),
            host=os.environ.get("MYSQL_HOST"),
            database=os.environ.get("MYSQL_DATABASE"),
        )

        openai_connector = OpenAIConnector(api_key=os.environ.get("OPENAI_API_KEY"))
        cls.tts = TextToSQL(mysql_connector, openai_connector)

    def test_convert_text_to_sql(self) -> None:
        self.assertEqual(
            self.tts.convert_text_to_sql(
                "Get me list of people whose last name is Torres."
            ),
            "SELECT * FROM person WHERE last_name = 'Torres'",
        )
