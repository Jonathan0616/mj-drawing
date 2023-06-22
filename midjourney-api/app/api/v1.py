from app.auth.routers.auth import router as auth_router
from app.auth.routers.user import router as user_router
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
)

router.include_router(auth_router)
router.include_router(user_router)
