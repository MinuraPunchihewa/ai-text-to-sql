import os
import unittest
from dotenv import load_dotenv

from ai_text_to_sql import TextToSQL

load_dotenv()


class TestMSSQLConnector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_convert_text_to_sql(self):
        pass