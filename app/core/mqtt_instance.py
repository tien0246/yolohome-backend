from app.services.mqtt_service import MQTTService
from threading import Lock

mqtt_service = MQTTService()
published_internal = set()
published_lock = Lock()