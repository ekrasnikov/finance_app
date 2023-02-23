from fastapi import APIRouter

from app.v1.users import controller

router = APIRouter()
router.include_router(controller.router, prefix='/users', tags=['users'])
