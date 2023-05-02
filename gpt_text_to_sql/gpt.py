import openai
from gpt_text_to_sql.connectors.database_connector_factory import DatabaseConnectorFactory


class GPT:
    """The main class for a user to interface with the OpenAI API.

    A user can add examples and set parameters of the API request.
    """
    def __init__(self,
                 connector_name,
                 connection_data,
                 engine='text-davinci-003',
                 temperature=0,
                 max_tokens=150,
                 top_p=1.0,
                 frequency_penalty=0.0,
                 presence_penalty=0.0,
                 stop=("#", ";")):
        self.connector = DatabaseConnectorFactory.build_connector(connector_name, connection_data)
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.stop = list(stop)

    def get_prime_text(self):
        """Formats all examples to prime the model."""
        prime_text = f"{self.connector.name} tables, with their properties:\n#\n"
        tables = self.connector.get_tables()
        for table in tables:
            columns = [column['name'] for column in self.connector.get_columns(table)]
            prime_text += f"# {table}(" + ", ".join(columns) + ")\n"

        prime_text += "#\n### "
        return prime_text

    def get_engine(self):
        """Returns the engine specified for the API."""
        return self.engine

    def get_temperature(self):
        """Returns the temperature specified for the API."""
        return self.temperature

    def get_top_p(self):
        """Returns the top_p specified for the API."""
        return self.top_p

    def get_frequency_penalty(self):
        """Returns the frequency_penalty specified for the API."""
        return self.frequency_penalty

    def get_presence_penalty(self):
        """Returns the presence_penalty specified for the API."""
        return self.presence_penalty

    def get_max_tokens(self):
        """Returns the max tokens specified for the API."""
        return self.max_tokens

    def craft_query(self, prompt):
        """Creates the query for the API request."""
        return self.get_prime_text() + prompt

    def submit_request(self, prompt):
        """Calls the OpenAI API with the specified parameters."""
        response = openai.Completion.create(engine=self.get_engine(),
                                            prompt=self.craft_query(prompt),
                                            max_tokens=self.get_max_tokens(),
                                            temperature=self.get_temperature(),
                                            top_p=self.get_top_p(),
                                            frequency_penalty=self.get_frequency_penalty(),
                                            presence_penalty=self.get_presence_penalty(),
                                            stream=False,
                                            stop=self.stop)
        return response

    def get_top_reply(self, prompt):
        """Obtains the best result as returned by the API."""
        response = self.submit_request(prompt)
        return response['choices'][0]['text']
