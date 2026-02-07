from models.app_base_model import AppBaseModel


class AuthUserModel(AppBaseModel):
    role: str

    email: str

    user_id: int

    token: str