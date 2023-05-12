# GPT-Text-to-SQL

GPT-Text-to-SQL is the Python package that makes querying databases as easy as asking questions in plain English. With this package, you don't need to know SQL to get the answers you need from your databases.

The package provides a simple interface for interacting with various databases. At the moment, SQLite, MySQL, MariaDB, and MS SQL Server are supported. These interfaces are called "Connectors" because they connect you to your data faster than you can say "SELECT * FROM table;".

## Installation
### With pip

Installing GPT-Text-to-SQL is as easy as pip-pip-pip:
```
pip install gpt_text_to_sql
```

## Usage

Using GPT-Text-to-SQL is so easy, you might even forget you're querying a database and start asking it what's the meaning of life, the universe, and everything. (Spoiler alert: it's 42, but you can still ask more questions if you want.)

First, import the package:
```
from gpt_text_to_sql import TextToSQL
```

Next, create an instance of the TextToSQL class:
```
tts = TextToSQL(
    'SQLite',
    {
        "database": "data/chinook.db"
    },
    os.environ.get("OPENAI_API_KEY")
)
```
To instantiate the TextToSQL class, you need to provide the following parameters:
- `connector_name`: The name of the database you want to connect to (e.g., SQLite, MySQL, MariaDB, MSSQL).
- `connection_data`: A dictionary containing the configuration parameters for the database connector (e.g., database, username, password).
- `openai_api_key`: Your OpenAI API key.

The keys required in the `connection_data` dictionary depend on the database connector you're using. For example, if you're using the SQLite connector, you only need to provide the path to the database file. If you're using the MySQL connector, you need to provide the host, port, username, password, and database name.
The required keys for each connector can be found in the documentation for that `Connector` class.

Additionally, given below are examples of how to instantiate the `TextToSQL` class for each of the supported database connectors:

### SQLite
```
```

### MySQL
```
```

### MariaDB
```
```

### MSSQL
```
```

Now that you've summoned the mystical TextToSQL class, you hold the power to query your database with ease:
```
tts.query("")
```
The `query` method returns a list of dictionaries, where each dictionary represents a row in the result set.

Why settle for a list of dictionaries when you can have a fancy pandas DataFrame? Use the `query_df` method to get the results you deserve:
```
tts.query_df("")
```