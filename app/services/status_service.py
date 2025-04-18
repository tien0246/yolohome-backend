from app.db.session import SessionLocal
from app.models.status import Status, StatusEnum
from app.schemas.status_schema import StatusInSchema
from sqlalchemy import desc

class StatusService:
    def create_status(self, s: StatusInSchema):
        db = SessionLocal()
        record = Status(s.device_id, s.type)
        db.add(record)
        db.commit()
        db.refresh(record)
        db.close()
        return record

    def create_status_direct(self, device_id: str, type: StatusEnum):
        db = SessionLocal()
        record = Status(device_id, type)
        db.add(record)
        db.commit()
        db.refresh(record)
        db.close()
        return record

    def get_latest_status(self, device_id: str):
        db = SessionLocal()
        status = db.query(Status).filter(Status.device_id == device_id).order_by(Status.timestamp.desc()).first()
        db.close()
        return status
