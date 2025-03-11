from fastapi import FastAPI
from contextlib import asynccontextmanager
import threading
from app.db.session import Base, engine
from app.routes import auth_route, device_route, sensor_route
from app.services.mqtt_service import MQTTService
from app.observers.sensor_subject import SensorSubject
from app.observers.store_observer import StoreObserver
from app.observers.threshold_observer import ThresholdObserver

Base.metadata.create_all(bind=engine)
store_observer = SensorSubject().attach(StoreObserver())
SensorSubject().attach(ThresholdObserver())
mqtt_service = MQTTService()

@asynccontextmanager
async def lifespan(app: FastAPI):
    thread = threading.Thread(target=mqtt_service.start)
    thread.start()
    yield
    mqtt_service.stop()
    thread.join()

app = FastAPI(lifespan=lifespan)
app.include_router(auth_route.router, prefix="/auth", tags=["auth"])
app.include_router(device_route.router, prefix="/api", tags=["device"])
app.include_router(sensor_route.router, prefix="/api", tags=["sensor"])
