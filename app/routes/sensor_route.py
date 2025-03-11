from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from app.schemas.sensor_data_schema import SensorDataInSchema, SensorDataOutSchema
from app.services.sensor_service import SensorService
from app.services.device_service import DeviceService
from app.services.auth_service import get_current_user

router = APIRouter()

@router.post("/sensor", response_model=SensorDataOutSchema)
def create_sensor_data(data: SensorDataInSchema, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(data.device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return SensorService().record_sensor_data(data)

@router.get("/sensor", response_model=List[SensorDataOutSchema])
def get_sensor_data(device_id: Optional[int] = None, limit: int = Query(100, ge=1), user=Depends(get_current_user)):
    if device_id:
        dev = DeviceService().get_device_by_id(device_id)
        if not dev or dev.user_id != user.id:
            raise HTTPException(status_code=403, detail="Unauthorized")
    return SensorService().get_all_sensor_data(device_id, limit)

@router.get("/sensor/check-alert", response_model=bool)
def check_alert_in_recent_5(device_id: int, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    last5 = SensorService().get_all_sensor_data(device_id, 5)
    return any(rec.alert for rec in last5)

@router.get("/sensors/time-range", response_model=List[SensorDataOutSchema])
def get_sensors_in_time_range(device_id: int, start: int, end: int, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return SensorService().get_by_time_range(device_id, datetime.fromtimestamp(start), datetime.fromtimestamp(end))