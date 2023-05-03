import os
import unittest
from dotenv import load_dotenv

from gpt_text_to_sql.text_to_sql import TextToSQL

load_dotenv()


class TestSQLiteConnector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tts = TextToSQL(
            'SQLite',
            {
                "db_file": "data/chinook.db"
            },
            os.environ.get("OPENAI_API_KEY")
        )

    def test_convert_text_to_sql(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get me a list of distinct genres."),
            "SELECT DISTINCT Name FROM genres"
        )