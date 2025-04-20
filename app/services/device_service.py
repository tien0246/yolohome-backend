from app.db.session import SessionLocal
from app.models.device import Device
from app.schemas.device_schema import DeviceCreateSchema, DeviceUpdateSchema
from fastapi import HTTPException, status
from app.models.user_log import UserLog

class DeviceService:
    def create_device(self, d: DeviceCreateSchema, user_id):
        db = SessionLocal()
        dev = Device(d.feed_id, user_id, d.name, d.type, d.location, d.min_value, d.max_value)
        existing_device = db.query(Device).filter(Device.feed_id==d.feed_id, Device.user_id==user_id).first()
        if existing_device:
            db.close()
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Device already exists")
        db.add(dev)
        db.flush()

        log = UserLog(user_id=user_id, device_id=dev.id, action="create device")
        db.add(log)

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

    def update_device(self, device_id, d: DeviceUpdateSchema, user):
        db = SessionLocal()
        dev = db.query(Device).filter(Device.id==device_id).first()
        if not dev:
            db.close()
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Device not found")
        if dev.user_id != user.id:
            db.close()
            raise HTTPException(status.HTTP_403_FORBIDDEN, "Unauthorized")

        if d.name is not None:
            dev.name = d.name
        if d.type is not None:
            dev.type = d.type
        if d.location is not None:
            dev.location = d.location
        if d.min_value is not None:
            dev.min_value = d.min_value
        if d.max_value is not None:
            dev.max_value = d.max_value

        log = UserLog(user_id=user.id, device_id=dev.id, action="update device")
        db.add(log)
        db.commit()
        db.refresh(dev)
        db.close()
        return dev
    
    def delete_device(self, device_id, user):
        db = SessionLocal()
        dev = db.query(Device).filter(Device.id == device_id).first()
        if not dev:
            db.close()
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Device not found")
        if dev.user_id != user.id:
            db.close()
            raise HTTPException(status.HTTP_403_FORBIDDEN, "Unauthorized")

        log = UserLog(user_id=user.id, device_id=dev.id, action="delete device")
        db.add(log)
        db.delete(dev)
        db.commit()
        db.close()