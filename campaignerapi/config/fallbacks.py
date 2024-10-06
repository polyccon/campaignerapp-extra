import os
from enum import Enum

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class SettingsFallbacks(Enum):
    SECRET_KEY = "this-is-not-a-secret-key"
    DATABASE_HOST = "db"
    DATABASE_NAME = "campaignerapi"
    DATABASE_PASSWORD = "not-a-password"
    DATABASE_USER = "not-a-user"
    DATABASE_PORT = 5432
    DATABASE_SSL = False
    DATABASE_ENGINE = "django.db.backends.postgresql"