from fastapi import APIRouter, Depends, HTTPException
from app.schemas.status_schema import StatusInSchema, StatusOutSchema
from app.services.status_service import StatusService
from app.services.device_service import DeviceService
from app.services.auth_service import get_current_user

router = APIRouter()

@router.post("/status", response_model=StatusOutSchema)
def create_status(s: StatusInSchema, user=Depends(get_current_user)):
    device = DeviceService().get_device_by_id(s.device_id)
    if not device or device.user_id != user.id:
        raise HTTPException(403, "Unauthorized")
    return StatusService().create_status(s)

@router.get("/status/{device_id}", response_model=StatusOutSchema)
def get_status(device_id: str, user=Depends(get_current_user)):
    device = DeviceService().get_device_by_id(device_id)
    if not device or device.user_id != user.id:
        raise HTTPException(403, "Unauthorized")
    status = StatusService().get_latest_status(device_id)
    if not status:
        raise HTTPException(404, "No status found")
    return status
