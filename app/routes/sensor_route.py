from fastapi import APIRouter, Depends
from app.schemas.sensor_data_schema import SensorDataInSchema, SensorDataOutSchema
from app.services.sensor_service import SensorService
from app.services.auth_service import get_current_user

router = APIRouter()

@router.post("/sensor", response_model=SensorDataOutSchema)
def create_sensor_data(data: SensorDataInSchema, user=Depends(get_current_user)):
    s = SensorService()
    return s.record_sensor_data(data)
