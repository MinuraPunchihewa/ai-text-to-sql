# AI-Text-to-SQL: Transforming Text Queries into SQL Magic ✨
Have you ever wished you could simply speak or type your queries in plain English, and poof! They magically turn into perfectly formatted SQL queries? Well, say hello to ai_text_to_sql - the enchanting Python package that brings your dream to life!

## Unleashing the Magic 🌟
### With pip

Installing AI-Text-to-SQL is as easy as pip-pip-pip:
```
pip install ai_text_to_sql
```

## Casting the Spell 🪄

To summon the power of AI-Text-to-SQL, follow these mystical steps:
1. Import the Data Connector: Begin by importing the required data connector of your choice. It's like selecting the perfect wand for your SQL sorcery!

2. Import the LLM Connector: Next, import the LLM (Language Learning Model) connector. This vital ingredient enhances the mystical abilities of ai_text_to_sql, enabling it to comprehend your text queries like a seasoned SQL wizard.

3. Instantiating TextToSQL: Now, it's time to weave your magic! Create an instance of TextToSQL by passing in the objects of the previously instantiated data connector and LLM connector. This mystical union forms the very heart of ai_text_to_sql, enabling it to interpret your words and craft elegant SQL incantations.

## Spellbinding Example Usage 🎩

```python
from ai_text_to_sql.data_connectors import SQLiteConnector
from ai_text_to_sql.llm_connectors import OpenAIConnector
from ai_text_to_sql.text_to_sql import TextToSQL

# Prepare your spell ingredients 
sqlite_connector = SQLiteConnector(database='chinook.db')
openai_connector = OpenAIConnector(api_key='YOUR_OPENAI_API_KEY')

# Weave the enchantment 🧙‍♂️✨
text_to_sql = TextToSQL(sqlite_connector, openai_connector)

# Utter your magical incantation 🗣️✨
text_query = "Find all the tracks written by AC/DC, including the track name, album title, and the artist name. Sort the results alphabetically by track name."

# Witness the spell's transformation 🔮✨
sql_query = text_to_sql.convert_text_to_sql(text_query)

# Unleash the magic upon the database directly 💾✨
results = text_to_sql.query(text_query)

# Store the results in a DataFrame for further sorcery 📊✨
df = text_to_sql.query_df(text_query)
```

To witness the enchanting powers of AI-Text-to-SQL in action, behold the following example usage with the SQLite data connector and OpenAI LLM connector.

## The Realm of Compatible Databases 🌐🏰

Within the enchanted realm of AI-Text-to-SQL, a variety of databases stand ready to be harmoniously united with your mystical text queries. Our sorcery extends its reach to the following realms of data:

| Database     | Status  |
|--------------|---------|
| SQLite       | ✅       | 
| PostgreSQL   | ✅       |
| MySQL        | ✅       |   
| MariaDB      | ✅       |   
| MS SQLServer | ✅       |   
| Oracle       | 🔜      |   
| MS Access    | 🔜      |
| Firebird     | 🔜      |   
| IBM Db2      | 🔜      |

Is your preferred database missing from our list? Don't worry! Suggestions for new data connectors are always welcome. Feel free to create an issue on the GitHub repository and maybe even submit a pull request!

## The Fellowship of Language Learning Models 🧠📚

In the mystical realm of AI-Text-to-SQL, an esteemed fellowship of Language Learning Models (LLMs) awaits to join forces with your magical text queries. Our sorcery encompasses the wisdom of the following LLM allies:

| LLM         | Status  |
|-------------|---------|
| OpenAI      | ✅       |
| Bard        | 🔜      |   
| HuggingFace | 🔜      |   

Excited about the potential of additional LLMs? If you have recommendations for new LLM connectors to integrate into AI-Text-to-SQL, please create an issue on the GitHub repository to share your ideas and take steps to contribute to the project!

## Contributing 🤝

Thank you for your interest in contributing to AI-Text-to-SQL! Contributions from the community are highly appreciated.

For detailed instructions on how to contribute to the project, please refer to the CONTRIBUTING.md file. It provides guidelines on reporting bugs, suggesting new features, making code improvements, and more.

Your contributions are valuable, and together, let's collaborate to enhance AI-Text-to-SQL and make it even more magical!

## License 📜

AI-Text-to-SQL is released under the GNU General Public License v3.0 (GPL-3.0). This means that you are free to use, modify, and distribute this package in compliance with the terms outlined in the license.

Embrace the spirit of open-source collaboration and together let's propel the world of text-to-SQL transformation forward!