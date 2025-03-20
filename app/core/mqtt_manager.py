import sys, json
from Adafruit_IO import MQTTClient
from app.utils.config import config
from app.observers.sensor_subject import SensorSubject

def connected(client):
    client.subscribe("temp")

def disconnected(client):
    sys.exit(1)

def message(client, feed_id, payload):
    try:
        data = json.loads(payload)
        if isinstance(data, dict) and data["key"] == feed_id:
            data = {"feed_id": feed_id, "value": data["data"]["value"]}
            SensorSubject().notify(data)
    except Exception:
        pass

def get_mqtt_client():
    c = MQTTClient(config.aio_username, config.aio_key)
    c.on_connect = connected
    c.on_disconnect = disconnected
    c.on_message = message
    return c
