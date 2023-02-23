from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from passlib.hash import pbkdf2_sha256


class User(BaseModel):
    id: UUID = uuid4()
    login: str
    hashed_password: str
    created_at: datetime = datetime.now()

    def create_user(self, login: str, password: str) -> 'User':
        hashed_password = self._hash_password(password)
        return User(login=login, password=hashed_password)

    @staticmethod
    def _hash_password(password: str) -> str:
        return pbkdf2_sha256.hash(password)

