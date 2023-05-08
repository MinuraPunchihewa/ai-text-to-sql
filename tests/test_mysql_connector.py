import os
import unittest
from dotenv import load_dotenv

from gpt_text_to_sql import TextToSQL

load_dotenv()


class TestMySQLConnector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tts = TextToSQL(
            'MySQL',
            {
                'user': os.environ.get("MYSQL_USER"),
                'port': os.environ.get("MYSQL_PORT"),
                'password': os.environ.get("MYSQL_PASSWORD"),
                'host': os.environ.get("MYSQL_HOST"),
                'database': os.environ.get("MYSQL_DATABASE")
            },
            os.environ.get("OPENAI_API_KEY")
        )

    def test_convert_text_to_sql(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get me list of people whose last name is Torres."),
            "SELECT * FROM person WHERE last_name = 'Torres'"
        )