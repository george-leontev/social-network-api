from datetime import datetime, timedelta, timezone
from hashlib import sha256
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
import jwt
from sqlalchemy.orm import Session
from database import get_db
from data_models.user_data_model import User
from models.auth_user_model import AuthUserModel
from models.signin_model import SignInModel

router = APIRouter()

@router.post("/sign-in", response_model=AuthUserModel)
def signin(body: SignInModel, db: Session = Depends(get_db)):
    account: User = db.query(User).where(body.email == User.email).first()

    if not account:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Не удалось войти в систему. Пользователь не найден.'
        )

    hashed_signin_password = sha256(body.password.encode(encoding="utf-8")).hexdigest()

    if hashed_signin_password == account.password:
        token = jwt.encode(
            {"exp": datetime.now(timezone.utc) - timedelta(days=1)}, account.password
        )

        return AuthUserModel(
            role="user",
            email=account.email,
            user_id=account.id,
            token=token
        )
