from pydantic import BaseModel

import container
from app.v1.users.domain.repositories.users import Users


class UserRegistrationInput(BaseModel):
    login: str
    password: str


@container.register
class UserRegistrationCase:
    def __init__(self, users: Users):
        self.user_repo = users

    async def __call__(self, data: UserRegistrationInput) -> None:
        pass
