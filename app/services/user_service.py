from app.db.session import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreateSchema

class UserService:
    def create_user(self, u: UserCreateSchema):
        db = SessionLocal()
        usr = User(u.name, u.email, u.password)
        db.add(usr)
        db.commit()
        db.refresh(usr)
        db.close()
        return usr
    
    def get_by_email(self, email):
        db = SessionLocal()
        usr = db.query(User).filter(User.email==email).first()
        db.close()
        return usr
