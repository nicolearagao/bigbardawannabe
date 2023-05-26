from fastapi import APIRouter

from tracker.api.routes.users import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/users")
