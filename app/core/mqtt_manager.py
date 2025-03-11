import sys, json
from Adafruit_IO import MQTTClient
from app.utils.config import config
from app.observers.sensor_subject import SensorSubject

def connected(client):
    client.subscribe("#")

def disconnected(client):
    sys.exit(1)

def message(client, feed_id, payload):
    print(payload)
    try:
        data = json.loads(payload)
        if not isinstance(data, dict):
            data = {"feed_id": feed_id, "value": float(data)}
        SensorSubject().notify(data)
    except Exception:
        SensorSubject().notify({"feed_id": feed_id, "value": float(payload)})

def get_mqtt_client():
    c = MQTTClient(config.aio_username, config.aio_key)
    c.on_connect = connected
    c.on_disconnect = disconnected
    c.on_message = message
    return c
