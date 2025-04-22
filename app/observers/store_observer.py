from app.observers.iobserver import IObserver
from app.db.session import SessionLocal
from app.models.device import Device
from app.models.sensor_data import SensorData
from app.services.status_service import StatusService
from app.models.status import StatusEnum

class StoreObserver(IObserver):
    def update(self, data):
        session = SessionLocal()
        try:
            feed_id = data.get("feed_id")
            val = data.get("value")
            print(f"Received data: {data}")
            device = session.query(Device).filter(Device.feed_id==feed_id).first()
            if device and val is not None:
                print(f"Storing data for device {device.id}: {val}")
                record = SensorData(device.id, val, (float(val) < device.min_value or float(val) > device.max_value))
                session.add(record)
                session.commit()
                StatusService().create_status_direct(device.id, StatusEnum.active)
        finally:
            session.close()