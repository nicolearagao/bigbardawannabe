from fastapi import APIRouter

from tracker.api.routes.users import router as user_router
from tracker.api.routes.daily_info import router as daily_info
from tracker.api.routes.fitness_metrics import router as fitness

router = APIRouter()

router.include_router(user_router, prefix="/users")
router.include_router(daily_info, prefix="/users")
router.include_router(fitness, prefix="/users")
