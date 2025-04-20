from fastapi import APIRouter, Depends
from typing import List
from app.schemas.device_schema import *
from app.services.device_service import DeviceService
from app.services.auth_service import get_current_user
from fastapi import HTTPException, status

router = APIRouter()

@router.get("/device", response_model=List[DeviceOutSchema])
def get_devices(user=Depends(get_current_user)):
    return DeviceService().get_devices_by_user(user.id)

@router.post("/device", response_model=DeviceOutSchema)
def create_device(d: DeviceCreateSchema, user=Depends(get_current_user)):
    if '_' in d.feed_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Feed ID cannot contain underscores")
    return DeviceService().create_device(d, user.id)

@router.patch("/device/{device_id}", response_model=DeviceOutSchema)
def update_device(device_id: str, d: DeviceUpdateSchema, user=Depends(get_current_user)):
    return DeviceService().update_device(device_id, d, user)

@router.delete("/device/{device_id}")
def delete_device(device_id: str, user=Depends(get_current_user)):
    DeviceService().delete_device(device_id, user)
    return {"detail": "Device deleted"}