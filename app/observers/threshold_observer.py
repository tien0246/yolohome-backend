from app.observers.iobserver import IObserver
from app.db.session import SessionLocal
from app.models.device import Device
from app.models.sensor_data import SensorData
from app.services.alert_service import AlertService

class ThresholdObserver(IObserver):
    def __init__(self):
        self.alert_service = AlertService()
    def update(self, data):
        session = SessionLocal()
        try:
            fid = data.get("feed_id")
            val = data.get("value")
            device = session.query(Device).filter(Device.feed_id==fid).first()
            if device and val is not None:
                if val < device.min_value or val > device.max_value:
                    rec = session.query(SensorData).order_by(SensorData.id.desc()).first()
                    if rec:
                        rec.alert = True
                        session.commit()
                    self.alert_service.send_alert(device.user_id, f"Device {device.name} out of range: {val}")
        finally:
            session.close()
