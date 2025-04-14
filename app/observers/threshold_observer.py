from app.observers.iobserver import IObserver
from app.db.session import SessionLocal
from app.models.device import Device
from app.models.sensor_data import SensorData
from app.models.user_log import UserLog
from app.services.alert_service import AlertService

class ThresholdObserver(IObserver):
    def __init__(self):
        self.alert_service = AlertService()
    def update(self, data):
        s = SessionLocal()
        try:
            fid = data.get("feed_id")
            val = data.get("value")
            dev = s.query(Device).filter(Device.feed_id==fid).first()
            if dev and val is not None:
                if val < dev.min_value or val > dev.max_value:
                    rec = s.query(SensorData).order_by(SensorData.id.desc()).first()
                    if rec:
                        rec.alert = True
                        s.commit()
                    self.alert_service.send_alert(dev.user_id, f"Device {dev.name} out of range: {val}")

                    log = UserLog(None, dev.user_id, dev.id, f"ALERT value={val}")
                    s.add(log)
                    s.commit()
        finally:
            s.close()
