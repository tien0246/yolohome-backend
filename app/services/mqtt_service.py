from app.core.mqtt_manager import get_mqtt_client
from app.utils.config import config

class MQTTService:
    def __init__(self):
        self.client = get_mqtt_client()
    def start(self):
        self.client.connect()
        self.client.loop_background()
    def stop(self):
        self.client.disconnect()
    def publish(self, feed_id, data):
        print(f"Publishing to {feed_id}: {data}")
        print(self.client.publish(feed_id, data))