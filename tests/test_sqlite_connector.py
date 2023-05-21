import os
import unittest
from dotenv import load_dotenv

from gpt_text_to_sql import TextToSQL

load_dotenv()


class TestSQLiteConnector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tts = TextToSQL(
            'SQLite',
            {
                "database": "data/chinook.db"
            },
            'GPT',
            os.environ.get("OPENAI_API_KEY")
        )

    def test_convert_text_to_sql(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get me a list of distinct genres."),
            "SELECT DISTINCT Name FROM genres"
        )

    def test_advanced_convert_text_to_sql(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get me the names of 5 Rock songs."),
            "SELECT Name \n"
            "FROM tracks \n"
            "INNER JOIN genres ON genres.GenreId = tracks.GenreId \n"
            "WHERE genres.Name = 'Rock' \n"
            "LIMIT 5"
        )

    def test_query(self):
        genres = self.tts.query("Get me a list of 5 distinct genres.")
        self.assertEqual(
            [genre[0] for genre in genres],
            ['Rock', 'Jazz', 'Metal', 'Alternative & Punk', 'Rock And Roll']
        )
