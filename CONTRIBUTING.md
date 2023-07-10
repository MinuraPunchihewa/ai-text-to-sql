## Code Contribution Guidelines 💻
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your changes to your fork.
6. Create a pull request.
7. Wait for your pull request to be reviewed.
8. Make any changes requested by the reviewer.
9. Wait for your pull request to be merged.
10. Celebrate your success! 🎉

### Guidelines for Contributing Data Connectors 💽
To contribute a new data connector, please follow these steps:
1. Create a new module in the data_connectors directory.
2. Create a new class in the module that inherits from the base DataConnector class.
3. Add the 'name' attribute to the new class to set the name of the connector.
4. Implement the create_connection() abstract method.
5. Implement the get_tables() and get_columns() methods if the database does not support the SQLAlchemy Inspector.
6. Add an import statement for the new class in the __init__.py file in the data_connectors directory.
7. Congratulations, data virtuoso! 🎉 Your mastery of data connectors has unlocked the gates to a realm of boundless data possibilities.

### Guidelines for Contributing LLM Connectors 🤖
To contribute a new LLM connector, please follow these steps:
1. Create a new module in the llm_connectors directory.
2. Create a new class in the module that inherits from the base LLMConnector class.
3. Add the 'name' attribute to the new class to set the name of the connector.
4. Implement the format_database_schema(), create_prompt() and get_answer() abstract methods.
5. Add an import statement for the new class in the __init__.py file in the llm_connectors directory.
6. Rejoice and let the Fellowship of Language Learning Models raise their virtual goblets in celebration! 🎉 Your mastery of LLM connectors has united the powers of AI language models, forging an alliance that transcends the boundaries of human-machine communication.