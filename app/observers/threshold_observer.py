from app.observers.iobserver import IObserver
from app.db.session import SessionLocal
from app.models.device import Device
from app.models.sensor_data import SensorData
from app.services.alert_service import AlertService

class ThresholdObserver(IObserver):
    def __init__(self):
        self.alert_service = AlertService()
    def update(self, data: dict):
        session = SessionLocal()
        try:
            feed_id = data.get("feed_id")
            value = data.get("value")
            device = session.query(Device).filter(Device.feed_id==feed_id).first()
            if device and value is not None:
                if value < device.min_value or value > device.max_value:
                    sensor_record = session.query(SensorData).order_by(SensorData.id.desc()).first()
                    if sensor_record:
                        sensor_record.alert = True
                        session.commit()
                    self.alert_service.send_alert(f"Device {device.name} out of range: {value}")
        finally:
            session.close()
