import os
import unittest
from dotenv import load_dotenv

from ai_text_to_sql import TextToSQL

load_dotenv()


class TestSQLiteConnector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tts = TextToSQL(
            'SQLite',
            {
                "database": "data/chinook.db"
            },
            api_key=os.environ.get("OPENAI_API_KEY")
        )

    def test_convert_text_to_sql(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get me a list of distinct genres."),
            "SELECT DISTINCT Name FROM genres"
        )

    def test_advanced_convert_text_to_sql_1(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get me the names of 5 Rock songs.").replace('\n', '').strip(),
            "SELECT Name \n"
            "FROM tracks \n"
            "INNER JOIN genres ON genres.GenreId = tracks.GenreId \n"
            "WHERE genres.Name = 'Rock' \n"
            "LIMIT 5".replace('\n', '').strip()
        )

    def test_advanced_convert_text_to_sql_2(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Find all the tracks written by AC/DC, including the track name, album title, and the artist name. Sort the results alphabetically by track name.").replace('\n', ' ').strip(),
            "SELECT t.Name AS Track, a.Title AS Album, ar.Name AS Artist \n"
            "FROM tracks t \n"
            "INNER JOIN albums a ON t.AlbumId = a.AlbumId \n"
            "INNER JOIN artists ar ON a.ArtistId = ar.ArtistId \n"
            "WHERE ar.Name = 'AC/DC' \n"
            "ORDER BY t.Name ASC".replace('\n', '').strip()
        )

    def test_query(self):
        genres = self.tts.query("Get me a list of 5 distinct genres.")
        self.assertEqual(
            [genre[0] for genre in genres],
            ['Rock', 'Jazz', 'Metal', 'Alternative & Punk', 'Rock And Roll']
        )
