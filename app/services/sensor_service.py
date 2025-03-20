from app.db.session import SessionLocal
from app.models.sensor_data import SensorData
from app.schemas.sensor_data_schema import SensorDataInSchema
from app.core.mqtt_instance import mqtt_service

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
        q = db.query(SensorData).order_by(SensorData.id.desc())
        if device_id:
            q = q.filter(SensorData.device_id==device_id)
        q = q.limit(limit)
        recs = q.all()
        db.close()
        return recs
    def get_by_time_range(self, device_id, start, end):
        db = SessionLocal()
        q = db.query(SensorData).filter(SensorData.device_id==device_id, SensorData.timestamp>=start, SensorData.timestamp<=end).order_by(SensorData.timestamp.desc())
        recs = q.all()
        db.close()
        return recs
