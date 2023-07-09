import os
import unittest
from dotenv import load_dotenv

from ai_text_to_sql.data_connectors.postgresql_connector import PostgreSQLConnector
from ai_text_to_sql.llm_connectors.openai_connector import OpenAIConnector
from ai_text_to_sql import TextToSQL

load_dotenv()


class TestPostgreSQLConnector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        postgresql_connector = PostgreSQLConnector(
            user=os.environ.get("POSTGRESQL_USER"),
            port=os.environ.get("POSTGRESQL_PORT"),
            password=os.environ.get("POSTGRESQL_PASSWORD"),
            host=os.environ.get("POSTGRESQL_HOST"),
            database=os.environ.get("POSTGRESQL_DATABASE"),
            schema=os.environ.get("POSTGRESQL_SCHEMA")
        )

        openai_connector = OpenAIConnector(
            api_key=os.environ.get("OPENAI_API_KEY")
        )
        cls.tts = TextToSQL(
            postgresql_connector,
            openai_connector
        )

    def test_convert_text_to_sql(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get me list of people whose last name is Torres."),
            "SELECT * FROM person WHERE last_name = 'Torres'"
        )