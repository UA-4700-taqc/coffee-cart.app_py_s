"""Configuration for resource management."""
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL: str = os.getenv("BASE_URL")
IMPLICIT_WAIT: int = int(os.getenv("IMPLICIT_WAIT", 0))
