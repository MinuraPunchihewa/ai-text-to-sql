# AI-Text-to-SQL: Transforming Text Queries into SQL Magic ✨

Have you ever wished you could simply speak or type your queries in plain English, and poof! They magically turn into perfectly formatted SQL queries? Well, say hello to AI-Text-to-SQL - the enchanting Python package that brings your dream to life!

## Unleashing the Magic 🌟

### With pip

Installing AI-Text-to-SQL is as easy as pip-pip-pip:

```
pip install ai_text_to_sql
```

## Casting the Spell 🪄

To summon the power of AI-Text-to-SQL, follow these mystical steps:

1. Import the Data Connector: Begin by importing the required data connector of your choice. It's like selecting the perfect wand for your SQL sorcery!

2. Import the LLM Connector: Next, import the LLM (Language Learning Model) connector. This vital ingredient enhances the mystical abilities of `ai_text_to_sql`, enabling it to comprehend your text queries like a seasoned SQL wizard.

3. Choose Your Path of Power:

- Conjuring the Core SQL Spell with `TextToSQL`: If you seek to transform text into SQL queries with the purest magic, invoke `TextToSQL`. This powerful incantation allows you to craft SQL queries from simple text, enabling you to summon the power of databases with ease and precision.

- Summoning the Enchanted Conversationalist with `TextToSQLChat` (New!): For those who desire the power of `TextToSQL` but with memory, `TextToSQLChat` remembers the context of previous queries. This allows you to build on past interactions, making your SQL spellcasting feel more like an ongoing conversation.

- Unlocking Advanced Sorcery with `TextToSQLAgent` (New!): If you seek a fully autonomous SQL assistant, `TextToSQLAgent` acts as an intelligent intermediary, orchestrating multi-step reasoning, handling follow-ups, and dynamically retrieving relevant information to craft the most precise queries. With this agent at your command, you can navigate complex data interactions with ease.

## Spellbinding Example Usage 🎩

### Basic Usage with `TextToSQL`

To witness the enchanting powers of AI-Text-to-SQL in action, behold the following example usage with the SQLite data connector and OpenAI LLM connector:

```python
from ai_text_to_sql.data_connectors import SQLiteConnector
from ai_text_to_sql.llm_connectors import OpenAIConnector
from ai_text_to_sql import TextToSQL


# Prepare your spell ingredients
sqlite_connector = SQLiteConnector(database='chinook.db')
openai_connector = OpenAIConnector(api_key='YOUR_OPENAI_API_KEY')

# Weave the enchantment 🧙‍♂️✨
text_to_sql = TextToSQL(sqlite_connector, openai_connector)

# Utter your magical incantation 🗣️✨
text_query = "Find all the tracks written by AC/DC, including the track name, album title, " \
             "and the artist name. Sort the results alphabetically by track name."

# Witness the spell's transformation 🔮✨
sql_query = text_to_sql.convert_text_to_sql(text_query)

# Unleash the magic upon the database directly 💾✨
results = text_to_sql.query(text_query)

# Store the results in a DataFrame for further sorcery 📊✨
df = text_to_sql.query_df(text_query)
```

### Conversational Usage with `TextToSQLChat`

The `TextToSQLChat` artifact is a conversational variant of `TextToSQL` that remembers the context of previous queries. Ready to engage in a dialogue with your SQL queries? Here's how to do it:

```python
from ai_text_to_sql.data_connectors import SQLiteConnector
from ai_text_to_sql.llm_connectors import OpenAIConnector
from ai_text_to_sql import TextToSQLChat


# Prepare your spell ingredients
sqlite_connector = SQLiteConnector(database='chinook.db')
openai_connector = OpenAIConnector(api_key='YOUR_OPENAI_API_KEY')

# Weave the enchantment 🧙‍♂️✨
text_to_sql = TextToSQLChat(sqlite_connector, openai_connector)

# Utter your magical incantation 🗣️✨
text_query = "Find all the tracks written by AC/DC, including the track name, album title, " \
             "and the artist name. Sort the results alphabetically by track name."

# Witness the spell's transformation 🔮✨
sql_query = text_to_sql.convert_text_to_sql(text_query)

# Unleash the magic upon the database directly 💾✨
results = text_to_sql.query(text_query)

# Store the results in a DataFrame for further sorcery 📊✨
df = text_to_sql.query_df(text_query)

# Continue the conversation with a follow-up query 🗣️✨
follow_up_query = "OK, now let's do Queen"
follow_up_results = text_to_sql.query(follow_up_query)
# OR
follow_up_df = text_to_sql.query_df(follow_up_query)
```

### Advanced Usage with `TextToSQLAgent`

The `TextToSQLAgent` is a more potent artifact for mastering the arcane arts of database interaction. Ready to harness its power? Here’s the incantation to summon it:

```python
from ai_text_to_sql.data_connectors import SQLiteConnector
from ai_text_to_sql.llm_connectors import OpenAIConnector
from ai_text_to_sql import TextToSQLAgent


# Prepare your spell ingredients
sqlite_connector = SQLiteConnector(database='chinook.db')
openai_connector = OpenAIConnector(api_key='YOUR_OPENAI_API_KEY')

# Weave the enchantment - this time with the TextToSQLAgent 🧙‍♂️✨
text_to_sql_agent = TextToSQLAgent(sqlite_connector, openai_connector)

# Utter your magical incantation 🗣️✨
text_query = "Find all the tracks written by AC/DC, including the track name, album title, " \
             "and the artist name. Sort the results alphabetically by track name."

# Unlock the agent's advanced powers to query the database directly 💾✨
response = text_to_sql_agent.query(text_query)
```

## The Realm of Compatible Databases 🌐🏰

Within the enchanted realm of AI-Text-to-SQL, a variety of databases stand ready to be harmoniously united with your mystical text queries. Our sorcery extends its reach to the following realms of data:

| Database     | Status |
| ------------ | ------ |
| SQLite       | ✅     |
| PostgreSQL   | ✅     |
| MySQL        | ✅     |
| MariaDB      | ✅     |
| MS SQLServer | ✅     |
| Oracle       | 🔜     |
| MS Access    | 🔜     |
| Firebird     | 🔜     |
| IBM Db2      | 🔜     |

Is your preferred database missing from the list? Don't worry! Suggestions for new data connectors are always welcome. Feel free to create an issue on the GitHub repository and maybe even submit a pull request!

## The Fellowship of Language Learning Models 🧠📚

In the mystical realm of AI-Text-to-SQL, an esteemed fellowship of Language Learning Models (LLMs) awaits to join forces with your magical text queries. Our sorcery encompasses the wisdom of the following LLM allies:

| LLM         | Status |
| ----------- | ------ |
| OpenAI      | ✅     |
| Bard        | 🔜     |
| HuggingFace | 🔜     |

Excited about the potential of additional LLMs? If you have recommendations for new LLM connectors to integrate into AI-Text-to-SQL, please create an issue on the GitHub repository to share your ideas and take steps to contribute to the project!

## Contributing 🤝

Thank you for your interest in contributing to AI-Text-to-SQL! Contributions from the community are highly appreciated.

For detailed instructions on how to contribute to the project, please refer to the CONTRIBUTING.md file. It provides guidelines on reporting bugs, suggesting new features, making code improvements, and more.

Your contributions are valuable, and together, let's collaborate to enhance AI-Text-to-SQL and make it even more magical!

## License 📜

AI-Text-to-SQL is released under the GNU General Public License v3.0 (GPL-3.0). This means that you are free to use, modify, and distribute this package in compliance with the terms outlined in the license.

Embrace the spirit of open-source collaboration and together let's propel the world of text-to-SQL transformation forward!
