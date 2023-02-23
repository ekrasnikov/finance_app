from fastapi import APIRouter, Body, Depends

from container import container
from app.v1.users.cases.registration import UserRegistrationInput, UserRegistrationCase

router = APIRouter()


@router.post(
    '/registration',
    summary='Registering a new user',
    response_description='null',
    status_code=201,
)
async def registration(
    data: UserRegistrationInput = Body(...),
    case: UserRegistrationCase = Depends(container.resolve(UserRegistrationCase))
) -> None:
    return await case(data)
