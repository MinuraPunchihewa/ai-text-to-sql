# AI-Text-to-SQL

AI-Text-to-SQL is the Python package that makes querying databases as easy as asking questions in plain English. With this package, you don't need to know SQL to get the answers you need from your databases.

The package provides a simple interface for interacting with various databases. At the moment, SQLite, MySQL, MariaDB, and MS SQL Server are supported. These interfaces are called "Connectors" because they connect you to your data faster than you can say "SELECT * FROM table;".

## Installation
### With pip

Installing AI-Text-to-SQL is as easy as pip-pip-pip:
```
pip install ai_text_to_sql
```

## Usage

Using AI-Text-to-SQL is so easy, you might even forget you're querying a database and start asking it what's the meaning of life, the universe, and everything. (Spoiler alert: it's 42, but you can still ask more questions if you want.)

First, import the package:
```
from ai_text_to_sql import TextToSQL
```

Next, create an instance of the TextToSQL class (this example uses SQLite)):
```
tts = TextToSQL(
    'SQLite',
    {
        "database": "your_database_file_name"
    },
    'GPT',
    'your_openai_api_key'
)
```
To instantiate the TextToSQL class, you need to provide the following parameters:
- `connector_name`: The name of the database you want to connect to (e.g., SQLite, MySQL, MariaDB, MSSQL).
- `connection_data`: A dictionary containing the configuration parameters for the database connector (e.g., database, username, password).
- `llm_name`: The name of the Large Language Model you want to use. This is an optional parameter and the default value is `GPT`. Currently, only the GPT model is supported, but more models like Bard will be added in the future.
- `api_key`: The API key for the Large Language Model. This is an optional parameter and the default value is `None`. Since the GPT model is currently the only supported model, this is essentially your OpenAI API key. If you don't provide an API key, the environment variable `OPENAI_API_KEY` will need to be configured.

The keys required in the `connection_data` dictionary depend on the database connector you're using. For example, if you're using the SQLite connector, you only need to provide the path to the database file. If you're using the MySQL connector, you need to provide the host, port, username, password, and database name.

The required keys for each connector can be found in the documentation for that `Connector` class.

Additionally, given below are examples of how to instantiate the `TextToSQL` class for each of the supported database connectors:

### SQLite
```
tts = TextToSQL(
    'SQLite',
    {
        "database": "your_database_file_name"
    },
    api_key='your_openai_api_key'
)
```

### MySQL
```
tts = TextToSQL(
    'MySQL',
    {
        'user': 'your_username',
        'port': '3306',
        'password': 'your_password',
        'host': 'your_host',
        'database': 'your_database_name'
    },
    api_key='your_openai_api_key'
)
```

### MariaDB
```
tts = tts = TextToSQL(
    'MariaDB',
    {
        'user': 'your_username',
        'port': '3306',
        'password': 'your_password',
        'host': 'your_host',
        'database': 'your_database_name'
    },
    api_key='your_openai_api_key'
)
```

### PostgreSQL
```
tts = tts = TextToSQL(
    'PostgreSQL',
    {
        'user': 'your_username',
        'port': '5432',
        'password': 'your_password',
        'host': 'your_host',
        'database': 'your_database_name'
    },
    api_key='your_openai_api_key'
)
```
Optionally, a `schema` parameter can be provided with the `connection_data` for `PostgreSQL`.

### MSSQL
```
tts = tts = TextToSQL(
    'MSSQL',
    {
        'user': 'your_username',
        'port': '1433',
        'password': 'your_password',
        'host': 'your_host',
        'database': 'your_database_name'
    },
    api_key='your_openai_api_key'
)
```
Optionally, a `schema` parameter can be provided with the `connection_data` for `MSSQL`.

Now that you've summoned the mystical TextToSQL class, you hold the power to query your database with ease:
```
tts.query("Get me the names of 5 Rock songs.")
```
The `query` method returns a list of dictionaries, where each dictionary represents a row in the result set.

Why settle for a list of dictionaries when you can have a fancy pandas DataFrame? Use the `query_df` method to get the results you deserve:
```
tts.query_df("Get me the names of 5 Rock songs.")
```

# License
This code is licensed under the GNU GENERAL PUBLIC LICENSE. See LICENSE.txt for details.