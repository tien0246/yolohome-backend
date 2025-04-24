from fastapi import APIRouter, HTTPException, Depends, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserCreateSchema, UserOutSchema
from app.services.auth_service import AuthService
from app.services.user_service import UserService

router = APIRouter()

@router.post("/signup", response_model=UserOutSchema)
def signup(user: UserCreateSchema):
    svc = UserService()
    if svc.get_by_email(user.email):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Email exists")
    return svc.create_user(user)

@router.post("/signin", response_model=TokenSchema)
def signin(form_data: OAuth2PasswordRequestForm = Depends(), expo_token: str | None = Form(None)):
    token = AuthService().login(form_data.username, form_data.password)
    if not token:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")
    if expo_token:
        svc = UserService()
        user = svc.get_by_email(form_data.username)
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")
        svc.update_expo_token(user.id, expo_token)
    return {"access_token": token, "token_type": "bearer"}