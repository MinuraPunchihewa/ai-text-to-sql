import os
import unittest
from dotenv import load_dotenv

from gpt_text_to_sql.text_to_sql import TextToSQL

load_dotenv()


class TestPostgreSQLConnector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tts = TextToSQL(
            'PostgreSQL',
            {
                'user': os.environ.get("POSTGRESQL_USER"),
                'port': os.environ.get("POSTGRESQL_PORT"),
                'password': os.environ.get("POSTGRESQL_PASSWORD"),
                'host': os.environ.get("POSTGRESQL_HOST"),
                'database': os.environ.get("POSTGRESQL_DATABASE")
            },
            os.environ.get("OPENAI_API_KEY")
        )

    def test_convert_text_to_sql(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get me list of people whose last name is Torres."),
            "SELECT * FROM person WHERE last_name = 'Torres'"
        )