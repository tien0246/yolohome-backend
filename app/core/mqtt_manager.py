import sys, json
from Adafruit_IO import MQTTClient
from app.utils.config import config
from app.observers.sensor_subject import SensorSubject
from app.core.mqtt_instance import published_internal, published_lock

def connected(client):
    client.subscribe("#")

def disconnected(client):
    sys.exit(1)

def message(client, feed_id, payload):
    try:
        data = json.loads(payload)
        if isinstance(data, dict) and data["key"] == feed_id:
            with published_lock:
                if (feed_id, data["data"]["value"]) in published_internal:
                    published_internal.remove((feed_id, data["data"]["value"]))
                    return
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