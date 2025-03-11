from app.observers.iobserver import IObserver
from app.db.session import SessionLocal
from app.models.device import Device
from app.models.sensor_data import SensorData

class StoreObserver(IObserver):
    def update(self, data: dict):
        session = SessionLocal()
        try:
            feed_id = data.get("feed_id")
            value = data.get("value")
            device = session.query(Device).filter(Device.feed_id==feed_id).first()
            if device and value is not None:
                record = SensorData(device_id=device.id, value=value)
                session.add(record)
                session.commit()
        finally:
            session.close()
