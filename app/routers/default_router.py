from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/")
def default_redirect():
    return RedirectResponse(url="/docs")
