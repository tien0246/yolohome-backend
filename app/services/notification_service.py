from exponent_server_sdk import PushClient, PushMessage, DeviceNotRegisteredError
from app.db.session import SessionLocal
from app.models.user import User

class NotificationService:
    def __init__(self):
        self.client = PushClient()

    def send(self, token: str, title: str, body: str, data: dict | None = None):
        msg = PushMessage(to=token, title=title, body=body, data=data or {})
        try:
            ticket = self.client.publish(msg)
            ticket.validate_response()
        except DeviceNotRegisteredError:
            s = SessionLocal()
            user = s.query(User).filter(User.expo_push_token == token).first()
            if user:
                user.expo_push_token = None
                s.commit()
            s.close()
        except Exception as e:
            print(f"Error sending notification: {e}")