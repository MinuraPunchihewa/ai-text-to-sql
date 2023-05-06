from typing import Optional, Dict, Text
from .mysql_connector import MySQLConnector


class MariaDB(MySQLConnector):
    name = 'MariaDB'

    def __init__(self, name: Text, connection_data: Optional[Dict]):
        super().__init__(name, connection_data)