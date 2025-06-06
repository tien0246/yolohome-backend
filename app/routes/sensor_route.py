from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import List, Optional
from datetime import datetime
from app.schemas.sensor_data_schema import SensorDataInSchema, SensorDataOutSchema
from app.schemas.alert_schema import AlertOutSchema
from app.services.sensor_service import SensorService
from app.services.device_service import DeviceService
from app.services.auth_service import get_current_user
router = APIRouter()

@router.get("/sensor", response_model=List[SensorDataOutSchema])
def get_sensor_data(device_id: Optional[str] = None, limit: int = Query(100, ge=1), user=Depends(get_current_user)):
    if device_id:
        dev = DeviceService().get_device_by_id(device_id)
        if not dev or dev.user_id != user.id:
            raise HTTPException(status.HTTP_403_FORBIDDEN, "Unauthorized")
    return SensorService().get_all_sensor_data(device_id, limit)

@router.get("/sensor/check-alert", response_model=bool)
def check_alert(device_id: str, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Unauthorized")
    last5 = SensorService().get_all_sensor_data(device_id, 5)
    return any(r.alert for r in last5)

@router.get("/sensor/time-range", response_model=List[SensorDataOutSchema])
def get_sensors_in_time_range(device_id: str, start: int, end: Optional[int] = None, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Unauthorized")
    end_dt = datetime.fromtimestamp(end) if end else datetime.utcnow()
    return SensorService().get_by_time_range(device_id, datetime.fromtimestamp(start), end_dt)

@router.get("/sensor/alerts", response_model=List[AlertOutSchema])
def get_alerts(user=Depends(get_current_user)):
    if not user:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Unauthorized")
    return SensorService().get_alerts_for_user(user.id)

@router.post("/sensor", response_model=SensorDataOutSchema)
def create_sensor_data(data: SensorDataInSchema, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(data.device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Unauthorized")
    return SensorService().record_sensor_data(data, dev.feed_id)