import os
import yaml


class ConfigParser:
    def __init__(self, file_path='config/config.yaml'):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path), 'r') as f:
            self.config_dict = yaml.safe_load(f)

    def get_config_dict(self):
        return self.config_dict