from app.db.session import SessionLocal
from app.models.device import Device
from app.schemas.device_schema import DeviceCreateSchema

class DeviceService:
    def create_device(self, d: DeviceCreateSchema, user_id):
        db = SessionLocal()
        dev = Device(d.feed_id, user_id, d.name, d.type, d.location, d.min_value, d.max_value)
        db.add(dev)
        db.commit()
        db.refresh(dev)
        db.close()
        return dev
    
    def get_devices_by_user(self, user_id):
        db = SessionLocal()
        devices = db.query(Device).filter(Device.user_id==user_id).all()
        db.close()
        return devices
    
    def get_device_by_id(self, device_id):
        db = SessionLocal()
        dev = db.query(Device).filter(Device.id==device_id).first()
        db.close()
        return dev
