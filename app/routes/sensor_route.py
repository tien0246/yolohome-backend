from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from app.schemas.sensor_data_schema import SensorDataInSchema, SensorDataOutSchema
from app.services.sensor_service import SensorService
from app.services.device_service import DeviceService
from app.services.auth_service import get_current_user
from app.services.mqtt_service import MQTTService

router = APIRouter()

@router.get("/sensor", response_model=List[SensorDataOutSchema])
def get_sensor_data(device_id: Optional[str] = None, limit: int = Query(100, ge=1), user=Depends(get_current_user)):
    if device_id:
        dev = DeviceService().get_device_by_id(device_id)
        if not dev or dev.user_id != user.id:
            raise HTTPException(403, "Unauthorized")
    return SensorService().get_all_sensor_data(device_id, limit)

@router.get("/sensor/check-alert", response_model=bool)
def check_alert(device_id: str, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(403, "Unauthorized")
    last5 = SensorService().get_all_sensor_data(device_id, 5)
    return any(r.alert for r in last5)

@router.get("/sensor/time-range", response_model=List[SensorDataOutSchema])
def get_sensors_in_time_range(device_id: str, start: int, end: Optional[int] = None, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(403, "Unauthorized")
    end_dt = datetime.fromtimestamp(end) if end else datetime.utcnow()
    return SensorService().get_by_time_range(device_id, datetime.fromtimestamp(start), end_dt)

@router.post("/sensor", response_model=SensorDataOutSchema)
def create_sensor_data(data: SensorDataInSchema, user=Depends(get_current_user)):
    dev = DeviceService().get_device_by_id(data.device_id)
    if not dev or dev.user_id != user.id:
        raise HTTPException(403, "Unauthorized")
    MQTTService.update(dev.feed_id, data.value)
    return SensorService().record_sensor_data(data)