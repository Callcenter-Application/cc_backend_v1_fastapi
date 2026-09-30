from fastapi import APIRouter, Depends
from api.controller.auth_controller import AuthController
from api.utils.session_util import get_session
from api.utils.auth_dependency import get_current_user
from sqlmodel import Session
from api.dto.auth_dto import LoginModel

router = APIRouter(prefix="/users", tags=["Auth"])
auth_controller = AuthController()

@router.post("/login")
async def login(login_model: LoginModel, session: Session = Depends(get_session)):
    user = auth_controller.login(login_model.email, login_model.password, session)
    return user

@router.post("/logout")
async def logout(payload: dict = Depends(get_current_user), session: Session = Depends(get_session)):
    return auth_controller.logout(payload, session)
