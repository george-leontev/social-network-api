from fastapi import APIRouter
from routers import auth_router, default_router

router = APIRouter(prefix="/api")

router.include_router(auth_router.router, tags=["Authentication"])
router.include_router(default_router.router, tags=["Default"])