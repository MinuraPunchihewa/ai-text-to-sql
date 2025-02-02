import os
from typing import Text

import yaml


class ConfigParser:
    """
    The class for parsing the configuration file.

    Parameters
    ----------
    file_path: Text
        The path to the configuration file.
    """

    def __init__(self, file_path: Text = "config/logging.yaml") -> None:
        with open(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path), "r"
        ) as f:
            self.config_dict = yaml.safe_load(f)

    def get_config_dict(self) -> dict:
        """
        Get the configuration dictionary.
        :return: The configuration dictionary.
        """
        return self.config_dict
