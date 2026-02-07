from models.app_base_model import AppBaseModel


class SignInModel(AppBaseModel):
    email: str

    password: str