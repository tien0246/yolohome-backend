from app.utils.config import config
from app.core.mqtt_manager import get_mqtt_client

class MQTTService:
    def __init__(self):
        self.client = get_mqtt_client()
    def start(self):
        self.client.connect()
        self.client.loop_background()
    def stop(self):
        self.client.disconnect()
    def publish(self, feed_id, data):
        feed_path = f"{config.aio_username}/feeds/{feed_id}"
        print(f"Publishing to {feed_path}: {data}")
        self.client.publish(feed_path, str(data))
