from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.jwt_manager import create_access_token, decode_access_token
from app.services.user_service import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        email = payload.get("sub")
        if not email:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")
        user = UserService().get_by_email(email)
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "User not found")
        return user
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid or expired token")

class AuthService:
    def login(self, email, password):
        user = UserService().get_by_email(email)
        if not user or user.password != password:
            return None
        return create_access_token({"sub": user.email})
