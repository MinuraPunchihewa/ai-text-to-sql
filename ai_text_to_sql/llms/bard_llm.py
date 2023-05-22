import os
import bardapi
from typing import Text, Dict, List

import logging
import logging.config

from ai_text_to_sql.llms.llm import LLM
from ai_text_to_sql.config_parser import ConfigParser
from ai_text_to_sql.connectors.connector import Connector

logging_config_parser = ConfigParser()
logging.config.dictConfig(logging_config_parser.get_config_dict())
logger = logging.getLogger()


class BardLLM(LLM):
    pass