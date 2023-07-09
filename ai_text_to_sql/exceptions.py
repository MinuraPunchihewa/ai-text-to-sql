
class ConnectionCreationException(Exception):
    """
    Raised when a connection cannot be created.
    """
    pass


class InsufficientParametersException(Exception):
    """
    Raised when insufficient parameters are provided to a connector for creating a connection.
    """
    pass


class NoMSSQLDriverException(Exception):
    """
    Raised when a MSSQL driver is not found for using the MSSQL connector.
    """
    pass


class UnsupportedDataConnectorException(Exception):
    """
    Raised when an attempt is made to use an unsupported data connector.
    """
    pass


class UnsupportedLLMConnectorException(Exception):
    """
    Raised when an attempt is made to use an unsupported LLM connector.
    """
    pass


class NoOpenAIAPIKeyException(Exception):
    """
    Raised when no OpenAI API key is provided for using the OpenAI connector.
    """
    pass