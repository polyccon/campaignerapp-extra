import os
from enum import Enum

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class SettingsFallbacks(Enum):
    SECRET_KEY = "this-is-not-a-secret-key"