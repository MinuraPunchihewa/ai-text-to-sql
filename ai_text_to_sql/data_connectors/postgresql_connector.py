from typing import Dict, Text

from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .data_connector import DataConnector


class PostgreSQLConnector(DataConnector):
    """
    The Connector class for PostgreSQL databases.

    Parameters:
    -----------
    connection_data : Dict
        A dictionary containing the configuration parameters for the PostgreSQL connection.
        The following keys are required:
            - user: The username to connect to the database.
            - password: The password to connect to the database.
            - host: The host name or IP address of the database server.
            - port: The port number of the database server.
            - database: The name of the database to connect to.

        The following keys are optional:
            - schema: The name of the schema to connect to.

    """

    name = 'PostgreSQL'

    def __init__(self, connection_data: Dict):
        super().__init__(connection_data)

    def create_connection(self):
        """
        Create a connection to a PostgreSQL database.
        :return: A SQLAlchemy engine object for the connection to the PostgreSQL database.
        """
        try:
            engine = create_engine(f"postgresql+psycopg2://{self.connection_data['user']}:"
                                 f"{self.connection_data['password']}@{self.connection_data['host']}:"
                                 f"{self.connection_data['port']}/{self.connection_data['database']}")

            if 'schema' in self.connection_data:
                session_factory = sessionmaker(bind=engine)
                Session = scoped_session(session_factory)
                session = Session()
                session.execute(text(f"SET search_path TO {self.connection_data['schema']}"))
                session.commit()

            return engine
        except KeyError as e:
            missing_param = str(e).strip("'")
            raise ValueError(f"Missing parameter in connection_data: {missing_param}.")