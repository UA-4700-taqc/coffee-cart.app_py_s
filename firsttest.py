"""Module for testing the application setup and core functionality."""
import os

from dotenv import load_dotenv

load_dotenv()  # читає .env файл

base_url = os.getenv("BASE_URL")
implicitly_wait = int(os.getenv("IMPLICITLY_WAIT"))

print(base_url, implicitly_wait)
