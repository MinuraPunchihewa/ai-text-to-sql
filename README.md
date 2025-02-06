# AI-Text-to-SQL: Transforming Text Queries into SQL Magic ✨

Have you ever wished you could simply speak or type your queries in plain English, and poof! They magically turn into perfectly formatted SQL queries? Well, say hello to AI-Text-to-SQL - the enchanting Python package that brings your dream to life!

## Unleashing the Magic 🌟

### With pip

Installing AI-Text-to-SQL is as easy as pip-pip-pip:

```
pip install ai_text_to_sql
```

## Casting the Spell: AI-Text-to-SQL in Action 🎩✨

To summon the power of AI-Text-to-SQL, follow these mystical steps and witness the enchantment unfold!

### Step 1: Prepare Your Spell Ingredients 🌟

Begin by importing the essential components for your SQL sorcery:

- **Import the Data Connector**: Choose the right data connector, like selecting the perfect wand for your SQL spellcasting.
- **Import the LLM Connector**: This vital ingredient enhances the mystical abilities of `ai_text_to_sql`, enabling it to comprehend your text queries like a seasoned SQL wizard.

Let's summon the SQLite and OpenAI connectors to embark on our magical SQL adventure:

```python
from ai_text_to_sql.data_connectors import SQLiteConnector
from ai_text_to_sql.llm_connectors import OpenAIConnector
```

Now, define the magical incantation you wish to transform into SQL:

```python
text_query = "Find all the tracks written by AC/DC, including the track name, album title, and the artist name. Sort the results alphabetically by track name."
```

### Step 2: Choose Your Path of Power 🌟

#### 🧙‍♂️ Conjuring the Core SQL Spell with `TextToSQL`

For those who seek to transform text into SQL queries with pure magic, invoke `TextToSQL`:

```python
from ai_text_to_sql import TextToSQL

sqlite_connector = SQLiteConnector(database='chinook.db')
openai_connector = OpenAIConnector(api_key='YOUR_OPENAI_API_KEY')

text_to_sql = TextToSQL(sqlite_connector, openai_connector)

# Witness the spell's transformation 🔮✨
sql_query = text_to_sql.convert_text_to_sql(text_query)

# Unleash the magic upon the database directly 💾✨
results = text_to_sql.query(text_query)

# Store the results in a DataFrame for further sorcery 📊✨
df = text_to_sql.query_df(text_query)
```

#### 🧙‍♀️ Summoning the Enchanted Conversationalist with `TextToSQLChat` (New!)

For those who desire the power of `TextToSQL` but with memory, `TextToSQLChat` allows ongoing dialogue with your SQL queries:

```python
from ai_text_to_sql import TextToSQLChat

text_to_sql = TextToSQLChat(sqlite_connector, openai_connector)

# Begin the conversation with the initial query 🗣️✨
results = text_to_sql.query(text_query)
# OR
df = text_to_sql.query_df(text_query)

# Continue the dialogue with a follow-up query 🗣️✨
follow_up_query = "OK, now let's do Queen"

follow_up_results = text_to_sql.query(follow_up_query)
# OR
follow_up_df = text_to_sql.query_df(follow_up_query)
```

#### 🌯 Unlocking Advanced Sorcery with `TextToSQLAgent` (New!)

For those who seek a fully autonomous SQL assistant, `TextToSQLAgent` orchestrates multi-step reasoning, follow-ups, and intelligent query crafting:

```python
from ai_text_to_sql import TextToSQLAgent

text_to_sql_agent = TextToSQLAgent(sqlite_connector, openai_connector)

# Engage the AI agent in a conversation 🤖✨
response = text_to_sql_agent.query(text_query)
```

With these powerful artifacts at your disposal, you are now equipped to master the arcane arts of AI-driven SQL spellcasting! 🌟🎉

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
