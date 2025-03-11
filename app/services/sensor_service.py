from app.db.session import SessionLocal
from app.models.sensor_data import SensorData
from app.schemas.sensor_data_schema import SensorDataInSchema

class SensorService:
    def record_sensor_data(self, data: SensorDataInSchema):
        db = SessionLocal()
        record = SensorData(device_id=data.device_id, value=data.value)
        db.add(record)
        db.commit()
        db.refresh(record)
        db.close()
        return record
