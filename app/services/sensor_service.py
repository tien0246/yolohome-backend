from app.db.session import SessionLocal
from app.models.sensor_data import SensorData
from app.models.device import Device
from app.schemas.sensor_data_schema import SensorDataInSchema
from app.core.mqtt_instance import mqtt_service
from sqlalchemy import select
from sqlalchemy.orm import joinedload

class SensorService:
    def record_sensor_data(self, data: SensorDataInSchema, feed_id):
        mqtt_service.publish(feed_id, data.value)
        db = SessionLocal()
        rec = SensorData(data.device_id, data.value)
        db.add(rec)
        db.commit()
        db.refresh(rec)
        db.close()
        return rec
    
    def get_all_sensor_data(self, device_id, limit):
        db = SessionLocal()
        q = db.query(SensorData).order_by(SensorData.timestamp.desc())
        if device_id:
            q = q.filter(SensorData.device_id==device_id)
        q = q.limit(limit)
        recs = q.all()
        db.close()
        return recs
    

    def get_alerts_for_user(self, user_id):
        db = SessionLocal()
        q = (
            db.query(
                SensorData.device_id,
                Device.name,
                SensorData.value,
                SensorData.timestamp
            )
            .join(Device, SensorData.device_id == Device.id)
            .filter(Device.user_id == user_id, SensorData.alert.is_(True))
            .order_by(SensorData.timestamp.desc())
        )
        recs = q.all()
        db.close()
        return recs