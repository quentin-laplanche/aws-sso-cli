import re

EMAIL_PATTERN = "^[^@]+@[^@]+\.[^@]+$"


class AWSAccount:

    def __init__(self, name, id, email):
        self.name: str = name
        self._id: int = id
        self._email: str = email

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value):
        if value < 0:
            return ValueError("Invalid AWS Account ID")
        self._id = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value):
        if not re.match(EMAIL_PATTERN, value):
            return ValueError("Invalid email")
        self._email = value


class AccountRole:

    def __init__(self, name, aws_account) -> None:
        self.name: str = name
        self.account: AWSAccount = aws_account
