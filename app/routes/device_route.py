from fastapi import APIRouter, Depends
from app.schemas.device_schema import DeviceCreateSchema, DeviceOutSchema
from app.services.device_service import DeviceService
from app.services.auth_service import get_current_user

router = APIRouter()

@router.post("/device", response_model=DeviceOutSchema)
def create_device(d: DeviceCreateSchema, user=Depends(get_current_user)):
    s = DeviceService()
    return s.create_device(d)
