## Contribution Guidelines 💻
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
4. Implement the `create_connection()` abstract method.
5. Implement the `get_tables()` and `get_columns()` methods if the database does not support SQLAlchemy Inspector.
6. Add an import statement for the new class in the `__init__.py` file in the data_connectors directory.
7. Add unit tests for the new data connector in the `tests` directory.
8. Add your new data connector to the list of supported databases in the README.md file.
9. Update the package version number in the `__about__.py` file.
10. Congratulations, data virtuoso! 🎉 Your mastery of data connectors has unlocked the gates to a realm of boundless data possibilities.

### Guidelines for Contributing LLM Connectors 🤖
To contribute a new LLM connector, please follow these steps:
1. Create a new module in the llm_connectors directory.
2. Create a new class in the module that inherits from the base LLMConnector class.
3. Add the 'name' attribute to the new class to set the name of the connector.
4. Implement the `format_database_schema()`, `create_prompt()` and `get_answer()` abstract methods.
5. Add an import statement for the new class in the `__init__.py` file in the llm_connectors directory.
6. Add unit tests for the new LLM connector in the `tests` directory.
7. Add your new LLM connector to the list of supported LLMs in the README.md file.
8. Update the package version number in the `__about__.py` file.
9. Rejoice and let the Fellowship of Language Learning Models raise their virtual goblets in celebration! 🎉 Your mastery of LLM connectors has united the powers of AI language models, forging an alliance that transcends the boundaries of human-machine communication.

## Setting Up the Local Environment 🛠️
To set up the local environment for AI-Text-to-SQL, please follow these steps:
1. Fork the repository.
2. Clone the forked repository.<br>
`git clone https://github.com/YourUsername/ai_text_to_sql.git`
3. Create a virtual environment with Python 3.9 or higher.<br>
`conda create -n ai_text_to_sql python=3.9`
4. Activate the virtual environment.<br>
`conda activate ai_text_to_sql`
5. Install the dependencies.<br>
`pip install -r requirements.txt`

## Running the Unit Tests 🧪
To run the unit tests, please follow these steps:
1. Activate the virtual environment you created.<br>
2. Run the unit tests. Unit tests are available for all data connectors and LLM connectors, however, the majority of the tests require a database connection to be set up. As a result, the only unit tests that can be run without a running server is the tests for SQLite with OpenAI. To run these tests, execute the following command:<br>
`python -m unittest discover tests -t tests/excluded_tests`

Note: Please ensure that you do include unit tests for any new data connectors or LLM connectors that you create. We can decide whether or not to include them in the main test suite later.

## Release Process 🚀
The release process for AI-Text-to-SQL is completely automated. Once a pull request is merged into the main branch, the GitHub Actions workflow will automatically run the unit tests and build the package. If the unit tests pass, the package will be published to PyPI. Please ensure that you update the package version number in the `__about__.py` file before creating a pull request.

