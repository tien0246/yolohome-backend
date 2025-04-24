from app.observers.iobserver import IObserver
from app.db.session import SessionLocal
from app.models.device import Device
from app.models.sensor_data import SensorData
from app.models.user import User
from app.services.notification_service import NotificationService

class ThresholdObserver(IObserver):
    def __init__(self):
        self.notifier = NotificationService()
    def update(self, data):
        s = SessionLocal()
        try:
            feed_id = data.get("feed_id")
            val = float(data.get("value"))
            dev = s.query(Device).filter(Device.feed_id==feed_id).first()
            print(f"Device: {dev.name} - Value: {val}")
            if dev and val is not None:
                if val < dev.min_value or val > dev.max_value:
                    user = s.query(User).filter(User.id == dev.user_id).first()
                    if user and user.expo_token:
                        self.notifier.send(
                            user.expo_token,
                            title=f"Alert: {dev.name}",
                            body=f"Sensor {dev.name} has exceeded the threshold at {val}",
                            data={"device_id": dev.id, "value": val}
                        )
        finally:
            s.close()