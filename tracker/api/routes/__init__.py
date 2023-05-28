from fastapi import APIRouter

from tracker.api.routes.users import router as user_router
from tracker.api.routes.daily_info import router as daily_info

router = APIRouter()

router.include_router(user_router, prefix="/users")
router.include_router(daily_info, prefix="/users")
