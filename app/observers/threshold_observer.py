from app.observers.iobserver import IObserver
from app.db.session import SessionLocal
from app.models.device import Device
from app.models.sensor_data import SensorData
from app.services.alert_service import AlertService

class ThresholdObserver(IObserver):
    def __init__(self):
        self.alert_service = AlertService()
    def update(self, data):
        s = SessionLocal()
        try:
            feed_id = data.get("feed_id")
            val = float(data.get("value"))
            dev = s.query(Device).filter(Device.feed_id==feed_id).first()
            if dev and val is not None:
                if val < dev.min_value or val > dev.max_value:
                    rec = s.query(SensorData).filter(SensorData.device_id == dev.id).order_by(SensorData.timestamp.desc()).first()
                    if rec:
                        rec.alert = True
                        s.commit()
                    self.alert_service.send_alert(dev.user_id, f"{dev.name}: {val}")
        finally:
            s.close()