"""User credentials module."""
from dataclasses import dataclass


@dataclass
class User:
    """Class representing a user."""

    name: str
    email: str


valid_user = User(name="test_user", email="testemail@gmail.com")
invalid_user_empty_name = User(name="", email="testemail@gmail.com")
invalid_user_empty_email = User(name="test_user", email="")
invalid_user_incorrect_email = User(name="test_user", email="@gmail.com")
