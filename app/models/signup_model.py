from pydantic import EmailStr
from models.app_base_model import AppBaseModel


class SignUpModel(AppBaseModel):
    user_name: str

    email: EmailStr

    password: str

    confirmed_password: str