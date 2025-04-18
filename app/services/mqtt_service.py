from app.core.mqtt_manager import get_mqtt_client
from app.core.mqtt_instance import published_internal, published_lock
class MQTTService:
    def __init__(self):
        self.client = get_mqtt_client()
    def start(self):
        self.client.connect()
        self.client.loop_background()
    def stop(self):
        self.client.disconnect()
    def publish(self, feed_id, data):
        with published_lock:
            published_internal.add((feed_id, data))
        self.client.publish(feed_id, data)