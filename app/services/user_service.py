from app.db.session import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreateSchema

class UserService:
    def create_user(self, u: UserCreateSchema):
        db = SessionLocal()
        user = User(name=u.name, email=u.email, password=u.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()
        return user
    def get_by_email(self, email: str):
        db = SessionLocal()
        user = db.query(User).filter(User.email==email).first()
        db.close()
        return user
