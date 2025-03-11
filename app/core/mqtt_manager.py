import sys
from Adafruit_IO import MQTTClient
from app.utils.config import config
from app.observers.sensor_subject import SensorSubject
import json

def connected(client):
    client.subscribe("#")

def disconnected(client):
    sys.exit(1)

def message(client, feed_id, payload):
    print(f"Feed ID: {feed_id}, Payload: {payload}")
    try:
        data = json.loads(payload)
        SensorSubject().notify(data)
    except:
        SensorSubject().notify({"feed_id": feed_id, "value": float(payload)})

def get_mqtt_client():
    c = MQTTClient(config.aio_username, config.aio_key)
    c.on_connect = connected
    c.on_disconnect = disconnected
    c.on_message = message
    return c
