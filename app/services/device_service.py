from app.db.session import SessionLocal
from app.models.device import Device
from app.schemas.device_schema import DeviceCreateSchema

class DeviceService:
    def create_device(self, d: DeviceCreateSchema):
        db = SessionLocal()
        device = Device(feed_id=d.feed_id, user_id=d.user_id, name=d.name, type=d.type, location=d.location, min_value=d.min_value, max_value=d.max_value)
        db.add(device)
        db.commit()
        db.refresh(device)
        db.close()
        return device
