import sys, json
from Adafruit_IO import MQTTClient
from app.utils.config import config
from app.observers.sensor_subject import SensorSubject

def connected(client):
    client.subscribe("#")

def disconnected(client):
    sys.exit(1)

def message(client, feed_id, payload):
    try:
        data = json.loads(payload)
        if isinstance(data, dict):
            data = {"feed_id": data["value"]["key"], "value": data["value"]["data"]["value"]}
            SensorSubject().notify(data)
    except Exception:
        print("Invalid data")

def get_mqtt_client():
    c = MQTTClient(config.aio_username, config.aio_key)
    c.on_connect = connected
    c.on_disconnect = disconnected
    c.on_message = message
    return c
